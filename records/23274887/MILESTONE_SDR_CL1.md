# SDR-CL1: First Model-Attribution Replay of a Registered Substrate Determinism Gauntlet Across LLMs

**Author:** Leon Calvin Long, II — SquirlOS Technologies LLC
**Date:** October 10, 2026
**Run model (pinned):** claude_sonnet_5_5 (pin stamp `battery_model_pin_SDR-CL1`)
**Prior certification model:** gemini_3_1_pro (SDR-D, Oct 7, 2026)

## SQUIRL OS RESEARCH DISCLOSURE — READ FIRST

This work was produced inside an AI-assisted, receipt-first research program (open-book doctrine: audit-and-correction, versioned amendments, append-only public ledger). Every claim below is backed by a timestamped, publicly committed receipt trail in the four-horsemen repository. Errors are disclosed, not erased. Limitations are load-bearing.

> **Prototype disclaimer:** This software is a prototype and is provided for educational and research purposes only. It is not intended for production use, commercial deployment, or safety-critical environments. All systems are experimental and may contain defects.

## What Was Done

On October 7, 2026, substrate D (SIM-D, a zero-lineage standard Squirrel OS v1.1 box on PQC rails) was certified under a preregistered determinism gauntlet (SDR-D): a public harness, a frozen seed (`SIMD-SDRD-20261007-SEED-0001`), and a committed checksum prediction (`9337c4fc7785b91d6a2ffcb00bb72a66bef37141308515d69c715278f0d2df3e`) published BEFORE the run, with six registered falsifiers.

On October 10, 2026, the identical public gauntlet was replayed end-to-end under a Claude Sonnet 5.5-pinned agent session (SDR-CL1). No harness byte was modified.

## Result: CONVERGED

- **Phase A (parity, 10x):** 10/10 runs at the registered checksum
- **Phase C (temporal independence, 3x):** 3/3 runs at the registered checksum
- **Phase B (replay determinism):** 6 seeded anomalies x 2 identical submissions; all decision tuples identical; exact-match playbook selection only
- **Total:** 13/13 checksums byte-identical to the prediction committed three days earlier, under a different orchestrating LLM

## What This Receipt Establishes

The deterministic substrate's outputs are **model-independent**: the same registered bytes emerged under a Gemini-pinned session (original certification) and a Claude-pinned session (this replay). The cage, not the language model, owns the output. Swap the engine; keep the receipt.

This is scoped evidence: it demonstrates model-independence for THIS registered gauntlet on THIS substrate under THESE two pinned orchestration contexts. It does not claim determinism for arbitrary LLM behavior outside the governed boundary.

## Disclosed Deviations (audit-and-correction doctrine)

1. Phase B decisions executed against the hub canonical playbook roster (exact anomaly_type match, lowest-record-id tie-break) rather than the SIM-D app-local anomaly-response; the SIM-D app-local runtime was unreachable from this session type. The determinism claim for Phase B therefore covers the canonical matching rule, not the SIM-D app-local execution path.
2. The harness `verify` mode hardcodes the original certification date (2026-10-07); the replay date is carried in the run metadata file.
3. SDR-CL1 is a supplementary labeled run, tracked separately from the 60-night battery series (N-B1..N-B3) per stream-separation doctrine.

## Provenance and Lineage

- Public harness (unmodified, replayable by any party): `github.com/LLong2026/squirrel-os-lindy-test` → docs/sim-d/sdrd_harness.py
- Registered prediction + falsifiers (committed before the original run): `github.com/LLong2026/squirrel-os-lindy-test` → docs/sim-d/PREREGISTRATION_SDR-D.md
- Battery ledger entries 0022-0024: `github.com/LLong2026/four-horsemen`
- Method covered by filed provisional 64/119,191 (deterministically governed probabilistic neural computation) and PQC/DQCO filings; governance layer per DCAI (64/157,915). No new mechanism claimed in this record.
- Information-theory lineage acknowledged: Nyquist (1924) → Hartley (1928) → Shannon (1948) → Kolmogorov (1965).

## Associated Records

- SDR-D receipt (original certification): DOI 10.5281/zenodo.23217495 (N-D1-ACK companion substrate line)
- First LLM Cage milestone: DOI 10.5281/zenodo.23265723
- Deterministic Caging of Probabilistic LLMs (architecture paper): DOI 10.5281/zenodo.23266727
- DCAI community: https://zenodo.org/communities/dcai

## Files In This Record

1. `MILESTONE_SDR_CL1.md` — this document
2. `SDR_CL1_RUN_METADATA.json` — model attribution, timestamps, disclosed deviations
3. `SIMD_SDR_D_RECEIPT.json` — full gauntlet receipt from the replay (phases A/B/C)
4. `sdrd_phase_ac.json` — raw parity and temporal checksums
5. `sdrd_phase_b.json` — raw replay decision tuples (12 records)

*This record follows the two-key curation protocol: drafted and vetted by the system (Gabriel), published on the owner's explicit GO (Oct 10, 2026).*
