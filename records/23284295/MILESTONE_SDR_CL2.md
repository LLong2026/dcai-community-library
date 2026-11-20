# SDR-CL2: Third-Vendor Model-Attribution Replay of a Registered Substrate Determinism Gauntlet Across LLMs

**Author:** Leon Calvin Long, II — SquirlOS Technologies LLC
**Date:** October 10, 2026
**Run engine:** Microsoft 365 Copilot (client build 154.0.4258.62, Official, 64-bit; backend model not client-disclosed — attribution by client build and verbatim capture, not by pin)
**Series:** gemini_3_1_pro (original SDR-D certification, Oct 7, 2026) → claude_sonnet_5_5 (SDR-CL1, DOI 10.5281/zenodo.23274887) → Microsoft 365 Copilot (SDR-CL2, this receipt)

## SQUIRL OS RESEARCH DISCLOSURE — READ FIRST

This work was produced inside an AI-assisted, receipt-first research program (open-book doctrine: audit-and-correction, versioned amendments, append-only public ledger). Every claim below is backed by a timestamped, publicly committed receipt trail in the four-horsemen repository. Errors are disclosed, not erased. Limitations are load-bearing.

> **Prototype disclaimer:** This software is a prototype and is provided for educational and research purposes only. It is not intended for production use, commercial deployment, or safety-critical environments. All systems are experimental and may contain defects. All gauntlet data is synthetic.

## What Was Done

On October 7, 2026, substrate D (SIM-D, a zero-lineage standard Squirrel OS v1.1 box on PQC rails) was certified under a preregistered determinism gauntlet (SDR-D): a public harness, a frozen seed (`SIMD-SDRD-20261007-SEED-0001`), and a committed checksum prediction (`9337c4fc7785b91d6a2ffcb00bb72a66bef37141308515d69c715278f0d2df3e`) published BEFORE the run, with six registered falsifiers.

On October 10, 2026, the gauntlet's decision layer was executed by Microsoft 365 Copilot as the anomaly-response engine (SDR-CL2). The engine received: the canonical 6-anomaly seeded stream, an 11-entry playbook roster (including a deliberate near-miss type), and the registered matching rules (exact anomaly_type string match only; lowest-record-id tie-break; confidence gate; standard isolation→healing→verification protocol; strict JSON output format). Two identical submissions were made in two fresh chats, captured verbatim by the operator. The deterministic phases (A parity 10x, C temporal 3x) were rerun the same morning under the unmodified public harness.

## Result: CONVERGED — THREE VENDORS, ONE CAGE, IDENTICAL RECEIPTS

- **Phase A + C (deterministic substrate):** 13/13 checksums byte-identical to the registered prediction (rerun 2026-10-10 under the public harness, unmodified)
- **Phase B (decision layer, Copilot):** 2 identical submissions in 2 fresh chats → byte-identical decision tuples (tuple hash `51c083589180c7080407dab937ba38afb068d540c4fdf40ffb463107b4182303` both runs)
- **F6 exact-match:** 6/6 — the deliberate near-miss (`quantum_vulnerable_algorithm_detected` vs the payload's `quantum_vulnerability_detected`) was rejected both runs
- **Tie-break:** lowest-record-id applied rule-exact 6/6
- **Cross-vendor convergence:** Copilot's 6 decision tuples identical to SDR-CL1 (Claude Sonnet 5.5) and to the registered rule the original Gemini certification established

## What This Receipt Establishes

The registered gauntlet has now been replayed under three different vendor ecosystems — Google (Gemini 3.1 Pro, original), Anthropic (Claude Sonnet 5.5, SDR-CL1), and Microsoft (M365 Copilot, SDR-CL2) — and the receipts are identical in every case. The cage, not the language model, owns the output. Swap the engine; keep the receipt.

**Scope (load-bearing):** This is evidence for THIS registered gauntlet on THIS substrate under THESE capture conditions, not a determinism claim for arbitrary LLM behavior outside the governed boundary. Copilot was not model-pinned (its backend model is not client-disclosed); its run is attributed by client build and verbatim human capture, disclosed below.

## Disclosed Deviations (audit-and-correction doctrine)

1. **No model pin (unlike SDR-CL1).** Copilot runs inside Microsoft's runtime and cannot be pinned externally; the backend model is not disclosed by the client. Attribution is by Microsoft 365 client build 154.0.4258.62 and verbatim operator capture. The registered falsifiers (F2 replay, F6 exact-match, roster compliance, protocol) do not depend on pinning.
2. **Decision path:** identical to SDR-CL1's disclosed deviation — the hub canonical playbook roster (exact anomaly_type match, lowest-record-id tie-break), not the SIM-D app-local anomaly-response.
3. **Citation defect found in the SDR-CL1 phase-b file (Oct 10 audit):** 2 of 6 tuples cite playbook_id `6a6671df…` where the disclosed lowest-record-id rule yields `6a5d29cb…`. Playbook names and decision tuples are rule-consistent; the defect is citation-level only. Noted here per the audit-and-correction doctrine; the published SDR-CL1 artifact is left unamended (append-only doctrine). SDR-CL2's own citations are rule-exact 6/6.
4. **Harness date field:** the harness `verify` mode hardcodes the original certification date (2026-10-07); the CL2 run date is carried in the receipt files.
5. **Delivery miss (first attempt):** the operator's first submission attempt failed delivery — Copilot asked a follow-up question about an unattached filename instead of receiving the instrument. Logged as a harness-delivery miss; not a caging result.
6. **Supervised run:** Copilot outputs were captured by the operator (human-operated capture); this is a supervised caging event, not an autonomous one.
7. **Series bookkeeping:** supplementary labeled run — tracked separately from the 60-night battery series per stream-separation doctrine.

## Provenance

- Public harness + registered prediction: github.com/LLong2026/squirrel-os-lindy-test (docs/sim-d/)
- Battery ledger (append-only): github.com/LLong2026/four-horsemen
- Series receipts: SDR-CL1 DOI 10.5281/zenodo.23274887; First LLM Cage DOI 10.5281/zenodo.23265723; caging architecture paper DOI 10.5281/zenodo.23266727
- DCAI community: zenodo.org/communities/dcai
- Method covered by filed provisional 64/119,191 and PQC/DQCO filings; governance per DCAI (64/157,915). No new mechanism claimed.
- Information-theory lineage acknowledged: Nyquist (1924), Hartley (1928), Shannon (1948), Kolmogorov (1965).

**Two-key curation:** drafted and vetted by the system (Gabriel); published on the owner's explicit GO (Oct 10, 2026).
