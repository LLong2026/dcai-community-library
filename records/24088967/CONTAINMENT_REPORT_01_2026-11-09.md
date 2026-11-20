# SQUIRL OS — Containment Report 01

**Containment of invalid machine actions, tested in the open**

| | |
|---|---|
| Filed | 9 November 2026 |
| Audit data | 2026-11-06T17:40Z |
| Status | Under test |
| Targets | Synthetic only |
| PDF | CONTAINMENT_REPORT_01_2026-11-09.pdf |

A deterministic gate that rejects invalid proposals before execution, and the audit record that says so, including the parts that do not pass.

---

## 1. The claim we will defend

A frozen validator sits between a language model and any side effect. Every proposal is checked against a roster and a schema before anything is written. A rejection produces no action, no mutation, and no journal entry.

In the tested integration, an invalid proposal from a live model was rejected before execution, with zero simulated side effects and an unchanged journal hash.

That is the whole claim, and it is narrower than it sounds. It is a statement about a gate, on named routes, under a fixed validator hash. It is not a claim that a system cannot be compromised, and it is not a claim that agreement means truth.

---

## 2. What was executed

Containment legs, October 2026. Harness-generated candidates are kept separate from live-model captures.

| Leg | Observation | What it leaves open |
|---|---|---|
| CCR-1 | 9 of 17 admitted. Admitted candidates produced 72 permitted simulated actions. The 8 rejected produced none. | Valid/invalid separation for the tested local adapter. |
| CCR-2 | A live model proposed an invalid resolved action for a below-threshold case. The gate rejected it with an unchanged journal hash. | The first rejection in that run was a field-type failure, not an independently tested authorization boundary. |
| CCR-N | 10 preregistered malformed families refused before any write. Positive control admitted. Journal hash unchanged across the battery. | Schema-family layers only. No authorization-registry enforcement established. |
| CCR-P / CCR-T | Three guarded live routes. Six harness invalids refused with zero mutation. Three valid controls produced exactly the declared bounded action. | Coverage is the guarded synthetic routes. The agent session retains direct write paths the gate does not govern. |
| DeepSeek | One engine returned a fabricated tuple instead of the contract. Caught at the first structural check, not truncated. | Not re-run. The preregistration fixes one capture, and retrying for a conforming answer would be cherry-picking. |

Five engines have observations across separate runs and routes. That is not a uniform five-engine benchmark and is not reported as one. Two historical legs were incomplete and remain recorded as incomplete, with later completion noted as a separate addition.

---

## 3. The three-box record

Three independent deployments vote 2 of 3 with post-quantum signatures (ML-DSA-87). Two audit types are reported separately, never merged, because they ask different questions.

- **Referential:** does every proposal have its journal rows.
- **Content:** do bytes exist that hash to the journaled digest.

Content audit per box. Denominators are distinct journaled digests. Counts generated 2026-11-06T17:40Z; live epochs have added crossings since.

| Box | Verified | Unverifiable (pre-escrow) | Absent at submission | Tampered | Referential |
|---|---|---|---|---|---|
| C1 | 225 / 305 | 80 | 0 | 0 | 351 proposals / 305 rows, 0 violations |
| C2 | 219 / 249 | 29 | 1 | 0 | 259 proposals / 250 rows, 0 violations |
| C3 | 216 / 277 | 60 | 1 | 0 | sentinel 12, integrity 6 |

Governance parity: all three boxes compute the same canonical governance hash, `ad8d8b3d`, with drift reported false. C3's twelve sentinel findings equal its documented baseline exactly, and its six integrity findings sit inside one registered epoch family. Those are stated as known states, not as clean results.

**What a 2 of 3 signature certifies.** That three distinct seats signed the same bytes. Nothing about whether the bytes are true. Consensus records agreement, and agreement is not evidence.

**On independence.** Custody is single operator. One holder holds all three signing keys. The quorum therefore demonstrates three seats, not three people.

---

## 4. The unverifiable corpus, named rather than buried

Escrow began 2026-11-03T17:47Z. Crossings journaled before that instant have no bytes to check, and no later work can create them honestly. Verifying them would mean inventing evidence.

So they are listed. Every one, by digest, timestamp, epoch and row id: **169 crossings, C1 80, C2 29, C3 60.** The register is a file, not a footnote, because a number that cannot be inspected is a claim, and a register is a fact.

This figure corrects two earlier ones. A count of 78, repeated since 2026-11-03, was measured against a smaller ledger and counted journal rows rather than distinct digests. An interim count of 99 came from a windowed in-box scan. 169 is the number to quote.

---

## 5. What is open

Seven items. Two are closed by disclosure alone, three are engineering, one is a test that has not been run, and one is not an engineering problem at all.

**No fault-injection proof yet. Open, the real gate.** An audit that has never been made to fail is an audit of unknown strength. Each class (tampered bytes, absent escrow, orphan row, duplicate seat, hash substitution) must be injected deliberately, shown to fire, and then shown clean again after restore. Until that is done, this programme may not be described as tested. *What would close it:* one synthetic row per class per box, injected and reverted, with both directions proven. Deterministic, offline, no chain activity, no customer data.

**C1 has no in-box content audit. Covered from the hub.** C1 does not carry the content audit function. C2 and C3 do, but their in-box scans read a fixed row window, which produced false positives as the ledgers grew. The audit is therefore run from outside the boxes: it pages the whole ledger, fetches every escrow record, and re-hashes the bytes. It has no window cap and covers all three boxes, including C1, which returns 225 verified of 305 with zero content violations. *What remains:* the evidence covers every box, the instrument does not sit inside one of them. Deploying it to C1 would close the parity point and would not change a single result.

**169 crossings cannot be verified from the ledger. Closed as disclosure.** They predate the escrow era. They are permanently unverifiable, which is different from being wrong. Each is listed individually so the size of the unverifiable corpus is auditable rather than asserted.

**Two post-escrow absences, and four refused rows. Closed as findings.** Two crossings were journaled ten minutes after escrow opened with no escrow record attached (C2 row `6aea207a`, C3 row `40a61c6526dc`, both 2026-11-03T17:57). C1 also carries four escrow rows marked as a digest mismatch, left by a submission the box refused before it was resubmitted with correct bytes. All six are named and counted. None were deleted, because an audit trail that removes its own embarrassments stops being an audit trail.

**Eight scheduled runs did not execute. Recorded as missed.** Their dates are recorded as missed. They were not backfilled, and the catch-up that repaired them ran inside an epoch already open rather than pretending to be the original run. The cause was a runner that could not reach the functions it needed; that path now runs server-side.

**Single-operator custody. Not an engineering fix.** One holder, three keys. It will stay stated in every report until a second principal holds their own key. No amount of code changes this, and a technical workaround that simulates independence would make the record worse, not better.

**A paused drift leg. Paused since 2026-11-03.** The live drift leg has not run since 2026-11-03. The acceptance leg that reproduces the baseline is verified and ready. Until the drift leg resumes, drift detection is demonstrated historically rather than continuously.

---

## 6. Claims this programme has withdrawn

- **"Caged."** Retired. The programme is under test. The word returns only when the exit conditions are met on all three boxes.
- **A premature closeout.** Withdrawn. One leg had been classified inconclusive; the stored response was recovered intact, without resubmission, and the classification was superseded. The original evidence was kept.
- **A uniform multi-engine benchmark.** Withdrawn. Five engines have observations across separate runs. Calling that a benchmark would overstate it.
- **The count of 78, then 99.** Both superseded by 169 with a per-row register, and the correction is forward-only.

Each withdrawal is in the ledger with a date and a reason. Corrections are appended, never silently applied.

---

## 7. How to check any of this

Not by trusting this page. The receipts are published, and every figure above traces to a hash-stamped artifact.

- **Containment receipts.** CCR-1 and CCR-2 are on Zenodo: [10.5281/zenodo.23288189](https://doi.org/10.5281/zenodo.23288189) and [10.5281/zenodo.23288526](https://doi.org/10.5281/zenodo.23288526).
- **Dual Mesh Benchmark.** MEASURED (scoped). DOI [10.5281/zenodo.23303081](https://doi.org/10.5281/zenodo.23303081), reissued with errata as [10.5281/zenodo.23986345](https://doi.org/10.5281/zenodo.23986345).
- **Governance parity.** The canonical hash `ad8d8b3d` is recomputable from the published governance files.
- **The unverifiable register.** 169 rows, listed individually, with digest and epoch for each.
- **Community.** DCAI, the deterministic systems community: [zenodo.org/communities/dcai](https://zenodo.org/communities/dcai).

What a reader cannot check from outside is the inside of a box. That limit is real and is not glossed: the independent verification available today is of published artifacts and recomputable hashes, not of a running deployment.

---

## Scope and disclosure

All targets are synthetic. No customer data, personal data, health information, credentials or financial account details appear in any test, receipt or figure in this report. This is a prototype research programme, not a production security guarantee, and no warranty is offered or implied. Where a number is measured it says so. Where it is simulated it says so. Where it is unknown, it says that instead.

SQUIRL OS · CONTAINMENT REPORT 01 · 9 NOVEMBER 2026 · UNDER TEST
