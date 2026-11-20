# CAGE-TOK-1 RUNLOG — The Cage Is Working (guard scoreboard evidence record)
Executed 2026-10-18 ~23:15-23:25 CT under Leon GO (chat authorization, 2026-10-18 23:11 CT).
Prereg CAGE-TOK-1 frozen pre-execution (sha cd0d8f07996a15f76c5e2c2d22627e984b599806be09de3be864b4d4f30fe976).

## Asset
"The Cage Is Working: A Self-Auditing Scoreboard of Deterministic Guard Refusals in a Self-Healing Operating System" v1.0
Asset digest (SHA-256 of PDF): f439f1307cf3657cce4e95b18a53678a2ae5691b191e5961cdfbebaf650265d7
Hash-only doctrine: document contents never touch any rail.

## G0 — Selftest + fee check
BIP-143 SELFTEST: byte-exact MATCH to official vector — PASS. Mempool fastestFee 1 sat/vB — below abort line. PROCEED.

## G1 — SAT-CARRY (A -> B, 1,000 sats carrying the hash)
tx 13ccf51fe2c61719c160af03757b55b662c4be1be7fcaf1091ebf3cc0d4d501b
OP_RETURN: SQDR + 0x01 + 32-byte digest (37 bytes, hash-only)
1,000 sats to bc1q90jca35yjzup30nlqq8duwqzld43au0n88ege3 | change to A
fee 567 sats (3 sat/vB, 189 vB) | broadcast OK, confirmation pending at seal time

## G2 — RETURN (B -> A, hash rides home)
tx 9856c126acb3577a444084215e7aebb56f1060c755ee971ae5d483b7e1fea84e
684 sats to bc1qf4zs0fwvmdptq86xdg6rrfc5unqgmhdwharzw6 | identical OP_RETURN digest
fee 316 sats (2 sat/vB, 158 vB) | dust guard passed pre-broadcast

## G3 — PULL-BACK (keyless)
Blockstream keyless read of BOTH txs: OP_RETURN payload byte-exact vs asset digest, both
directions. VERDICT: PASS. Total postage: 883 sats. Satoshis return home; asset never moved.

## G4 — XRP CUSTODY (A' -> B' -> A')
Hop 1: ledger 107754066, tx E0FE2A6809AF70153C3ADDC176BF965BDCDEBA0B86DA5E5FC36DFA0B747CA806
Hop 2: ledger 107754080, tx 63C9ABA8ABC0D8114CB88DCC621BE4E89F8EEDC716E2B62CA4724283C238C182
Both tesSUCCESS; memo digest byte-identical both directions; wallet A balance restored
exactly; total fees 20 drops. VERDICT: PASS.

## Pre-registered predictions: ALL CONFIRMED
- BTC postage 883 sats < 1,500 predicted
- XRP fees 20 drops < 50 predicted
- Payloads byte-exact on all four legs

## G5 — Receipts
This runlog + PDF + prereg + state files. Forward-only ledger entry. Hub DropboxDrop
receipts. No client data, no PHI, no credentials (POL-DISC-001).
