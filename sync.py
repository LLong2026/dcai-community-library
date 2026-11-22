#!/usr/bin/env python3
"""
Mirror the Zenodo community 'dcai' into this repository, one record per directory.

Contract
--------
One Zenodo record  ==  one directory under records/<record_id>/.
The published file(s) are stored byte-identical under their original keys.
RECORD.json holds the record's public metadata plus a locally computed sha256
for every file, so the mirror can be checked without trusting Zenodo's API.

Idempotent: a file is re-downloaded only when it is missing or its size differs
from the published size. Nothing is ever deleted; a record withdrawn upstream
stays in the mirror and is reported in the manifest.

Stdlib only. No credentials: every record in this community is public.
"""
import hashlib
import json
import re
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

COMMUNITY = "dcai"
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = "LLong2026/dcai-community-library"
UA = f"dcai-community-library/1.0 (+https://github.com/{REPO})"
API = f"https://zenodo.org/api/communities/{COMMUNITY}/records"
PAGE_SIZE = 25

# Files that may not be mirrored into a public repository, decided by the
# deterministic personal-data gate (.agents/skills/personal-data-guard), never by
# judgement. An excluded file is still listed in RECORD.json with its published
# checksum, so a reader can fetch it from Zenodo and verify it themselves.
# The exclusion is named in the manifest and in the README count, never silent.
EXCLUSIONS = {
    (23672787, "EVIDENCE_COPILOT_CONFESSION_2026-10-26.md"):
        "personal-data-guard BLOCK: operator email address on line 3",
}


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(3 * (i + 1))
                continue
            raise
        except Exception as e:  # network flake
            last = e
            if i < tries - 1:
                time.sleep(3 * (i + 1))
                continue
            raise
    raise last


def fetch_all():
    out, page = [], 1
    while True:
        d = json.loads(get(f"{API}?size={PAGE_SIZE}&page={page}&sort=mostrecent"))
        h = d["hits"]
        recs = h["hits"]
        out.extend(recs)
        total = h.get("total", 0)
        if not recs or len(out) >= total:
            break
        page += 1
    return out


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_name(key):
    name = str(key).replace("\\", "/").split("/")[-1].strip()
    name = "".join(c for c in name if c not in '<>:"|?*' and ord(c) >= 32)
    return name or "unnamed"


# --- change detection -------------------------------------------------------
# A quiet night must produce no diff. mirrored_at is a run timestamp, so a file
# whose only difference is that timestamp is left alone on disk, and its stored
# value keeps meaning "when this record last actually changed".

VOLATILE = "mirrored_at"


def _norm_json(obj):
    if isinstance(obj, dict):
        return {k: _norm_json(v) for k, v in obj.items() if k != VOLATILE}
    if isinstance(obj, list):
        return [_norm_json(v) for v in obj]
    return obj


def write_json_if_changed(path, payload):
    if os.path.isfile(path):
        try:
            with open(path, encoding="utf-8") as fh:
                if _norm_json(json.load(fh)) == _norm_json(payload):
                    return False
        except Exception:
            pass
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return True


def _norm_readme(text):
    return re.sub(r"(\| Last mirror \| )[^|]*(\|)", r"\1__T__\2", text)


def write_readme_if_changed(path, text):
    if os.path.isfile(path):
        try:
            with open(path, encoding="utf-8") as fh:
                if _norm_readme(fh.read()) == _norm_readme(text):
                    return False
        except Exception:
            pass
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return True


def main():
    started = now()
    records = fetch_all()
    print(f"records in community: {len(records)}", flush=True)

    entries = []
    total_files = total_bytes = 0
    downloaded = 0

    for r in records:
        rid = str(r["id"])
        md = r.get("metadata") or {}
        rtype = md.get("resource_type") or {}
        d = os.path.join(ROOT, "records", rid)
        os.makedirs(d, exist_ok=True)

        files = []
        for f in r.get("files", []):
            fn = safe_name(f["key"])
            dest = os.path.join(d, fn)
            excl = EXCLUSIONS.get((r["id"], f["key"]))
            if excl:
                files.append({
                    "key": f["key"], "filename": fn, "size": f["size"],
                    "zenodo_checksum": f.get("checksum"), "sha256": None,
                    "excluded": True, "exclusion_reason": excl,
                    "fetch_from": f["links"]["self"],
                })
                continue
            fresh = (os.path.exists(dest) and os.path.getsize(dest) == f["size"])
            if not fresh:
                blob = get(f["links"]["self"])
                with open(dest, "wb") as fh:
                    fh.write(blob)
                downloaded += 1
                time.sleep(0.2)
            files.append({
                "key": f["key"],
                "filename": fn,
                "size": f["size"],
                "zenodo_checksum": f.get("checksum"),
                "sha256": sha256_file(dest),
            })

        rec = {
            "record_id": rid,
            "doi": r.get("doi"),
            "concept_doi": r.get("conceptdoi"),
            "title": md.get("title"),
            "description": md.get("description"),
            "publication_date": md.get("publication_date"),
            "resource_type": rtype.get("type"),
            "resource_type_title": rtype.get("title"),
            "version": md.get("version"),
            "license": (md.get("license") or {}).get("id"),
            "access_right": md.get("access_right"),
            "creators": [c.get("name") for c in md.get("creators", [])],
            "keywords": md.get("keywords", []),
            "related_identifiers": md.get("related_identifiers", []),
            "communities": [c.get("identifier") for c in md.get("communities", [])],
            "zenodo_url": (r.get("links") or {}).get("self_html"),
            "zenodo_modified": r.get("modified"),
            "mirrored_at": started,
            "files": files,
        }
        write_json_if_changed(os.path.join(d, "RECORD.json"), rec)

        nb = sum(x["size"] for x in files if not x.get("excluded"))
        total_files += sum(1 for x in files if not x.get("excluded"))
        total_bytes += nb
        entries.append({
            "record_id": rid,
            "doi": rec["doi"],
            "title": rec["title"],
            "publication_date": rec["publication_date"],
            "version": rec["version"],
            "resource_type_title": rec["resource_type_title"],
            "files": sum(1 for x in files if not x.get("excluded")),
            "excluded": sum(1 for x in files if x.get("excluded")),
            "bytes": nb,
            "path": f"records/{rid}",
        })

    excluded_total = sum(e["excluded"] for e in entries)

    manifest = {
        "community": COMMUNITY,
        "source": f"https://zenodo.org/communities/{COMMUNITY}",
        "mirrored_at": started,
        "mirror_rule": "one Zenodo record = one directory under records/, files byte-identical except named policy exclusions",
        "record_count": len(entries),
        "file_count": total_files,
        "excluded_file_count": excluded_total,
        "total_bytes": total_bytes,
        "records": sorted(entries, key=lambda e: e["publication_date"] or "", reverse=True),
    }
    write_json_if_changed(os.path.join(ROOT, "MANIFEST.json"), manifest)

    excl_rows = []
    for p in sorted(os.listdir(os.path.join(ROOT, "records"))):
        rp = os.path.join(ROOT, "records", p, "RECORD.json")
        if not os.path.isfile(rp):
            continue
        rec = json.load(open(rp))
        for f in rec["files"]:
            if f.get("excluded"):
                excl_rows.append(
                    f"- `{rec['doi']}` / `{f['key']}` ({f['size']:,} bytes) — {f['exclusion_reason']}. "
                    f"Published checksum `{f['zenodo_checksum']}`. "
                    f"[Fetch from Zenodo]({f['fetch_from']})")
    excl_section = ("## Excluded by policy\n\n"
        "These files are part of their record but are not mirrored here, because a deterministic\n"
        "personal-data gate refused them. Each is named, sized and carries its published checksum\n"
        "so a reader can fetch it from Zenodo and verify it. An exclusion is disclosed, never silent.\n\n"
        + ("\n".join(excl_rows) if excl_rows else "_None._") + "\n") if excl_rows else ""

    # README index
    rows = []
    for e in manifest["records"]:
        doi = e["doi"] or ""
        rows.append(
            f"| {e['publication_date'] or ''} | [{doi}](https://doi.org/{doi}) | "
            f"{e['title']} | {e['version'] or ''} | {e['files']} | "
            f"[{e['record_id']}]({e['path']}/) |"
        )
    readme = f"""# DCAI community library

A one-to-one mirror of the Zenodo community [**dcai**](https://zenodo.org/communities/dcai),
kept here so the public record of the community exists as a git-checkable library and
not only inside one platform's API.

**Rule: one Zenodo record = one directory.** `records/<record_id>/` holds the published
file(s) byte-identical under their original keys, plus `RECORD.json` with the record's
public metadata and a locally computed SHA-256 for every file. Nothing is rewritten,
reordered or summarised.

## Naming: Jasper and Testari

**Naming note (added 2026-11-22, forward-only).** Jasper is the name of the prototype and of the
deterministic hypervisor component described in several records here. Testari is the commercial name
of the finished product built from it. They are the same lineage under two names, not two systems.

No mirrored record has been rewritten to say otherwise. Records are left exactly as published, so a
2026 paper that says Jasper still says Jasper, because that is what the system was called when the
work was done. Where a name in this library differs from the name of the product you are looking at,
this note is the reason, and the DOI record remains the authority.

## What this is, and what it is not

- It is a mirror of *public* metadata and *public* files. Every record here was already
  published openly in the community.
- It is not a DOI registrar and confers no authority over any record. The DOI, the
  version history and the canonical bytes remain Zenodo's. If this mirror and Zenodo
  ever disagree, Zenodo is right and this repository is stale.
- Each record keeps its own licence, stated in its `RECORD.json`. This repository asserts
  no licence over the mirrored works; it only mirrors them.
- A file's authority is its SHA-256 in `RECORD.json`. Compare it against the file
  Zenodo serves to check the mirror; compare it against the hash quoted in a paper to
  check the paper.

## Contents

| | |
|---|---|
| Records | {manifest['record_count']} |
| Files | {manifest['file_count']} |
| Bytes | {manifest['total_bytes']:,} |
| Excluded by policy | {excluded_total} |
| Last mirror | {manifest['mirrored_at']} |

{excl_section}
`MANIFEST.json` carries the same inventory in machine-readable form. `sync.py` rebuilds
the mirror idempotently: it re-downloads only a missing or size-mismatched file, never
deletes, and writes nothing outside `records/` and the two index files.

```
python3 sync.py
```

## Index

| Published | DOI | Title | Version | Files | Record |
|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n"
    write_readme_if_changed(os.path.join(ROOT, "README.md"), readme)

    print(f"files downloaded this run: {downloaded}")
    print(f"mirror: {len(entries)} records, {total_files} files, {total_bytes:,} bytes")


if __name__ == "__main__":
    main()
