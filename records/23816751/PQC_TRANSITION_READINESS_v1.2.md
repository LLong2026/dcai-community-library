# PQC Transition Readiness

**SQUIRL OS Technologies LLC** · Prepared 2026-10-30 · Version 1.2 · Prototype research record

This document records the post-quantum cryptography (PQC) transition position of the SQUIRL OS
prototype against the standards and deadlines in force as of October 30, 2026. It states what the
standards require, what has been measured, and where the gap is. It claims no certification and
no compliance attestation.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-30 | Initial record against NISTIR 8547 final, EO 14412, OMB M-26-15, CNSA 2.0 |
| 1.1 | 2026-10-30 | Signature canonical raised from ML-DSA-65 to ML-DSA-87. SLH-DSA reclassified: FIPS 205 compliant but NOT approved for any NSS use. CNSA 2.0 conformance table added. Prior version retained in record history |
| 1.2 | 2026-10-30 | **Correction.** Version 1.1 stated key establishment had migrated to ML-KEM-1024. Measurement shows hybrid X25519MLKEM768, which is ML-KEM-768, and no ML-KEM-1024 anywhere. Signature migration now implemented and measured rather than planned. Component inventory added |

---

## 1. What changed on October 27, 2026

NIST published the final version of **NISTIR 8547, Transition to Post-Quantum Cryptography
Standards**, and withdrew the November 12, 2024 draft the same day.

The two headline dates survived. Quantum-vulnerable public-key algorithms are deprecated after
2030 and disallowed under NIST standards and guidelines after 2035. What changed is who falls
under the first date:

| Topic | Nov 2024 draft | Oct 2026 final |
|---|---|---|
| 112-bit classical (RSA-2048, P-224) | Deprecated after 2030, disallowed 2035 | Unchanged |
| 128-bit classical (P-256, P-384, RSA-3072, Ed25519) | No deprecation step, disallowed 2035 | **Deprecated after 2030**, disallowed 2035 |
| Hybrid key establishment | Not addressed | **FIPS 140-validatable** if at least one input is from an approved scheme |
| Second KEM | One or more alternatives expected | **HQC** named, standard in development |
| Default ML-KEM parameter set | Not addressed | **ML-KEM-768** recommended as default |

A deployment on P-256 or RSA-3072 is no longer "fine until 2035". It is a deprecated algorithm
after 2030, which under NIST's own definition means usable at assessed risk with a documented
decision attached. Vendor material dated before October 27, 2026 should be re-checked.

---

## 2. The governing dates

| Date | Requirement | Reaches |
|---|---|---|
| 2027-01-01 | CNSA 2.0 acquisition gate: new National Security System acquisitions must be CNSA 2.0 compliant | Defense contractors and DIB suppliers selling into an NSS |
| 2030-12-31 | Key establishment migrated on federal high-value assets and high-impact systems (EO 14412 + OMB M-26-15). Same date all approved classical strengths become deprecated under IR 8547 | Federal agencies and their supply chain |
| 2031-12-31 | Digital signatures migrated on the same systems | Same |
| 2035 | Classical public-key disallowed under NIST standards and guidelines (NSM-10 outer goal) | Anyone building on NIST standards |

Harvest-now-decrypt-later is why key establishment moves first. Signature migration carries no
equivalent retroactive exposure, which is why it holds the later date.

---

## 3. CNSA 2.0 conformance: the actual suite

CNSA 2.0 is not "any post-quantum algorithm". It is a named suite, and NSA's FAQ is explicit that
conformance follows the FIPS text rather than the algorithm's historical label.

| Function | CNSA 2.0 requirement | SQUIRL OS canonical |
|---|---|---|
| Symmetric block cipher | AES-256, all classification levels (FIPS 197) | AES-256 |
| Hashing | SHA-384 or SHA-512 (FIPS 180-4) | SHA-384 / SHA-512 |
| Key establishment | ML-KEM-1024, all classification levels (FIPS 203) | ML-KEM-1024 |
| Digital signatures | ML-DSA-87, all classification levels (FIPS 204) | ML-DSA-87 |
| Firmware / software validation | LMS or XMSS only, per SP 800-208. HSS and XMSSMT not allowed | Open item |
| HashML-DSA (pre-hash mode) | Not permitted at present | Not used |
| SLH-DSA (formerly SPHINCS+) | **Not part of CNSA 2.0. Not approved for any use in NSS** | See section 4 |

Two consequences follow directly from the NSA text and are the reason this record was revised:

1. **ML-DSA-65 does not satisfy CNSA 2.0.** The suite names ML-DSA-87 at every classification
   level. Category 3 is a commercial choice, not a defense choice.
2. **SLH-DSA is not a fallback.** Being hash-based and being approved are different things. NSA
   states plainly that SLH-DSA is not approved for any use in NSS, and that for firmware and
   software validation the only approved hash-based options are LMS or XMSS.

A third consequence concerns naming. An implementation calling itself CRYSTALS-Kyber or
CRYSTALS-Dilithium that does not conform to FIPS 203 or 204 is not CNSA 2.0 compliant, whatever it
is called. Conformance is a property of the FIPS text, not of the label.

---

## 4. Where SQUIRL OS stands

| Item | Measured state | Position |
|---|---|---|
| Key establishment | Hybrid **X25519MLKEM768** offered on both hosts, measured by TLS group enumeration. **ML-KEM-1024 not offered** | Post-quantum and ahead of the 2030 line, but **one parameter set below CNSA 2.0**, which names ML-KEM-1024 at every level |
| Signature canon | Raised to ML-DSA-87 (category 5) on 2026-10-30 | Canon now matches CNSA 2.0 |
| Signature implementation | ML-DSA-87 implemented and measured: public key 2,592 bytes, signature 4,627 bytes, roundtrip true, matching FIPS 204. Sign and verify dispatch on each key record's own type; keys issued earlier stay verifiable at ML-DSA-65 | **Met in code, not yet deployed.** Live instances keep the previous parameter set until redeploy and key rotation |
| Stateless hash signatures | SLH-DSA-SHA2-256f, FIPS 205 compliant | **Not usable in NSS.** Remains valid for non-NSS use only |
| Firmware / software validation | No LMS or XMSS implementation recorded | **Open**, required for an NSS firmware path |
| Hybrid key establishment | In use in transport: X25519 with ML-KEM-768 | Permitted and FIPS 140-validatable when at least one input is approved. Vendor default rather than project selection |
| Non-migratable systems | Not yet inventoried | Required by IR 8547 final |

## 5. Correction to version 1.1: key establishment

Version 1.1 recorded that transport key establishment had moved to ML-KEM-1024 at PQC-MIG-1, and
described the position as "at the CNSA 2.0 parameter level". That was wrong, and this version
corrects it rather than leaving it standing in a record that is being read.

**What was measured.** TLS group enumeration against both public hosts:

| Host | Grade | Post-quantum group offered | ML-KEM-1024 offered |
|---|---|---|---|
| squirlos-technologies.com | A | X25519MLKEM768 | No |
| science.squirlos-technologies.com | A+ | X25519MLKEM768 | No |

**What is true.** Post-quantum key establishment is genuinely present. X25519MLKEM768 is a hybrid of
classical X25519 with ML-KEM-768. It is not a claim about a plan; it is negotiated today.

**What is not true.** It is not ML-KEM-1024. The parameter set in use is one notch below the one
CNSA 2.0 names. ML-KEM-768 satisfies the NIST default recommendation; it does not satisfy CNSA 2.0.

**Attribution matters here.** X25519MLKEM768 is the content delivery network's default hybrid group.
It was not selected by this project, and no configuration change of ours would raise it to 1024.
Whether ML-KEM-1024 is obtainable at all depends on the network offering a 384-bit hybrid, which is a
vendor question rather than an engineering task. Recording this as a project achievement would have
been the inflation this document exists to avoid. Recording it as absent would also have been wrong.

**Method, stated so it can be repeated.** Group enumeration via SSL Labs, which reports offered
groups including post-quantum ones. A local `openssl s_client` probe was run first and returned
`X25519`, but OpenSSL 3.0.20 cannot offer ML-KEM groups, so that result described the client as much
as the server. It was discarded in favour of the enumeration rather than cited as evidence.

---

## 6. Signature migration: implemented and measured

Version 1.1 recorded the canon change and correctly warned that a canon change is not a code change.
Version 1.2 closes that: the implementation now matches the canon, and the parameters were measured
rather than assumed.

| Parameter set | Public key | Secret key | Signature | Roundtrip |
|---|---|---|---|---|
| ML-DSA-87 | 2,592 bytes | 4,896 bytes | 4,627 bytes | true |
| ML-DSA-65 | 1,952 bytes | 4,032 bytes | 3,309 bytes | true |
| Cross-set (ML-DSA-65 signature against ML-DSA-87 key) | | | | **false** |

Those figures match the FIPS 204 tables, which is the evidence that the library is doing what the
label says. The cross-set result is why the implementation dispatches on each key record's own
recorded type instead of guessing a parameter set: the two sets are not interchangeable, and a guess
would have produced silent verification failures.

The HMAC-SHA256 construction that previously stood in for a signature, under a key type naming
ML-DSA, has been deleted rather than relabelled. Surviving rows that carry it are refused with an
explicit reason.

---

Blunt statement of the boundary: the signature requirement is now met in code and not yet deployed,
so until redeploy and key rotation, running instances keep the previous parameter set. Key
establishment is genuinely post-quantum and one parameter set below the CNSA 2.0 requirement, at a
setting the network chose. Neither of those is a completed transition. Both are now measured facts
rather than assertions, which is the only improvement this version claims.

---

## 5. What is not built on

- **Pre-standard FALCON.** The IETF drafts state that FALCON and the final FN-DSA (FIPS 206) are
  not compatible. Building on FALCON now guarantees rework.
- **HQC.** Selected as the named backup key encapsulation mechanism, standard in development as
  FIPS 207. Referenced as a hedge, never implemented as a dependency.
- **SLH-DSA in any NSS context.** See section 3.
- **Any classical-only path as a default.** Deprecation after 2030 makes every such path a
  documented risk decision rather than a neutral default.

---

## 6. Dual Mesh Benchmark, MEASURED (scoped)

| Metric | Value | Scope |
|---|---|---|
| Anomaly lookup | 267x speedup (800 ms to 3 ms) | Dual mesh, deterministic layer |
| Topology | 25 active nodes (5 read, 13 interconnect, 7 write) | Fixed reference topology |
| Agents | 10, communicating collision-free | Same topology |
| Architecture patents | 3 covering the mesh | 64/119,191; 64/114,746; 64/145,825 |

Scoped per the telemetry composition correction (DOI 10.5281/zenodo.23812238), which disclosed the
split between organic and battery-injected rows in earlier telemetry reporting. Figures are stated
for the scope named in the row and are not generalized to production loads.

---

## 7. Method

Algorithm status, suite membership, dates and sizes come from NISTIR 8547 (final, 2026-10-27),
FIPS 197, FIPS 180-4, FIPS 203, FIPS 204, FIPS 205 (final, 2024-08-13), NIST SP 800-208,
Executive Order 14412, OMB M-26-15, and the NSA CNSA 2.0 FAQ (October 2026 revision). PQC-MIG-1 is
an internal migration record. Suite and deadline statements are reproducible from those sources.
Position statements in section 4 are specific to this prototype and are not independently certified.

---

## Disclaimer

SQUIRL OS is a prototype provided for educational and research purposes. It is not intended for
production use, commercial deployment, or safety-critical environments. This document is a
technical readiness record, not a compliance certification, audit opinion, or warranty of fitness
for any purpose. Algorithm guidance changes; verify against current NIST and NSA publications
before relying on any statement here.

Patent Reference: JASPER, Provisional Patent Application No. 64/114,746, filed July 18, 2026.
Inventor: Leon Calvin Long II.

Contact: support@squirlos-technologies.com
