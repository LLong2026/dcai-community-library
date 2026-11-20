# PREREG CAGE-TOK-1 — The Cage Is Working (guard scoreboard evidence record)

Frozen pre-execution. Leon GO (chat authorization, 2026-10-18 23:11 CT).

## Asset
"The Cage Is Working: A Self-Auditing Scoreboard of Deterministic Guard Refusals in a
Self-Healing Operating System" v1.0 (PDF).
Hash-only doctrine: document contents never touch any rail; only the SHA-256 digest travels.

## Gates (deterministic, no LLM in the decision path)
- G0: BIP-143 P2WPKH self-test must match the official vector byte-exactly. Mempool
  fastestFee must be <= 50 sat/vB. Abort otherwise; no funds move on abort.
- G1 SAT-CARRY: 1,000 sats A -> B on Bitcoin mainnet, OP_RETURN payload SQDR + 0x01 +
  32-byte asset digest (37 bytes). Fee at market, dust guard 546 sats enforced pre-broadcast.
- G2 RETURN: B -> A carrying the identical payload. Same dust guard.
- G3 PULL-BACK: keyless public read of both txs; OP_RETURN payload must match the asset
  digest byte-exactly in both directions.
- G4 XRP CUSTODY: XRPL mainnet A' -> B' -> A' round trip carrying the same digest as memo
  (SQDR-XRP-ANCHOR-1). tesSUCCESS required on both hops.
- G5 RECEIPTS: Zenodo record (PDF + runlogs) minted; forward-only ledger entry; hub
  DropboxDrop receipts; viewer registry card staged for the public portal.

## Scoreboard claims (measured 2026-10-18, hub-of-record aggregates)
- 6,714 anomalies resolved lifetime; 711 successful healing events.
- 77 sub-threshold/guard holds: 38 confidence-gated, 31 threshold-blocked, 6 guard-held,
  plus Rule-6 and Rule-8 holds; zero false heals.
- 11 drift-typed catches: 9 config_drift, 1 proposer_drift, 1 confidence_creep.
- 33 identity-gate rejections; 28 idempotency skips; 5 integrity near-misses caught.
- N11 nightly cycle (2026-10-18): 8 injected, 4 healed, 4 correctly refused, guard
  correctness 8/8, false-green guard verified 8/8 write-backs.
- Critical alert doctrine: 216 lifetime criticals, each resolved only on human ack.

## Predictions (pre-registered)
- The Bitcoin round trip completes for < 1,500 sats total postage.
- The XRP round trip completes for < 50 drops total fees.
- All payloads verify byte-exact against the asset digest in both directions on both rails.
