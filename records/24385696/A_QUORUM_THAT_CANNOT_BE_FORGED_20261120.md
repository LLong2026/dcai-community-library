---
title: "A quorum that cannot be forged"
summary: "Paper (v0.3) on the Conclave crossing gate: what an adopter actually gets, the four legs of building a safer AI, the four defect classes the five-arm battery found in deployed code, and the measurements that now certify it. Published; concept DOI 10.5281/zenodo.24385596, v0.3 version DOI 10.5281/zenodo.24385683."
---

> **Published v0.3, 2026-11-20.**
> Concept DOI 10.5281/zenodo.24385596, which always resolves to the newest version.
> This version: 10.5281/zenodo.24385683. Version 0.2: 10.5281/zenodo.24385597.
> Repo copy in four-horsemen-public/docs/receipts/.
> v0.3 adds section 2, which states in outcome terms what the gate buys. v0.2 reported the
> falsifications and left the purchase implied.

# A quorum that cannot be forged: building a safer AI by making it falsifiable

**Draft v0.2 — 2026-11-20. Journey structure. Internal, not published. Two-key gate not yet cleared.**
Leon Calvin Long, II — Squirrel OS Technologies LLC

---

## Abstract

This paper is not a claim to have made a safe AI. It is an account of what happened when one was
built to be falsified, and it reports the falsifications.

The work began with a narrow ambition: not a better model, but a better system around one. That
ambition produced four legs over roughly a year: a cage whose behaviour is measured by adversarial
probes rather than by the model's own assurances; a grounding check that refuses a claim unless it
resolves to a hashed artifact with a matching span; an approval path that binds a human's intent to one
exact state and makes the approval unusable afterwards; and a crossing gate requiring distinct
post-quantum seat signatures over escrowed payload bytes, backed by an audit that recomputes the whole
relation from stored state.

The result that matters is not that the last leg passed its tests. It is that the last leg, when
finally measured, was broken in four ways, and that the measurements which broke it are the same
measurements that now certify it. A quorum counted vote rows instead of distinct seats and never read
the vote value, so one assent plus one abstention agreed. A vote function verified a signature and then
discarded it, so every row it wrote was unsigned. A vote row omitted the one field its own audit
needed to choose a verification contract, so 24 correct signatures were reported invalid. A proposal
path never held the payload bytes, so a payload that did not hash to its own digest was accepted.

Three of those four were silences. The system did not fail loudly; it reported clean. We describe how
each was found, what each cost, and the reporting discipline that keeps a clean audit count from being
read as a clean system: every audit verdict in this paper is accompanied by the count of records it
could not reach.

We make no primacy claim. The components are old. What we claim is one specific combination and one
transferable habit: a gate that states what it cannot verify, in the same sentence as what it can.

What it buys is narrower than safety and more useful than assurance. An organisation that adopts this
can show a third party, from a receipt alone, that a given effect was authorised by a named person
against one exact state, that no agent's own judgement entered the path, that the approval cannot be
reused, and that the keys doing the authorising never sat on the server. It also inherits the four
questions that catch a governance system reporting green while broken.


Two limits are stated here rather than buried in a limits section, because both bear on how the result should be read. The V2 vote contract binds the payload and the seat but not the vote value, so a signed row does not by itself prove what the seat voted. And every seat private key is held by one custodian, so 2-of-3 certifies that three distinct keys signed, not that three independent people consented.
## 1. The ambition, stated plainly

The goal was never a model that would not do harm if asked. That framing has been tried and it does not
survive contact with an adversary who can ask differently. The goal was a system in which a model's
output cannot become an effect without passing gates that do not consult the model.

That decision has a cost, and the cost is the subject of this paper: once the model is not trusted to
judge itself, every judgement must be made by something that can be wrong in a way you can detect. Each
of the four legs below is an attempt to build such a thing, and each attempt failed at least once in a
way worth reporting.

## 2. What this buys

A paper about falsification reads, section by section, as a list of things that did not work. That
reading is fair to the method and unfair to the result, so the result is stated here, in outcome terms,
before the journey.

**A third party can check what your AI did without trusting you, and without access to your systems.**
Every action this gate permits produces a receipt whose bytes are reproducible outside the system that
made it: `printf '%s' '<payload_canonical>' | sha256sum` returns the digest the receipt claims. Bundles
are signed with ML-DSA-87 and re-verify as INTACT or fail outright. An auditor, a customer or a sponsor
holding nothing but the bundle can establish what was approved, by whom, over which state, and whether
it was altered afterwards. What they have today, from almost every vendor, is an assurance.

**An approval is spent by use.** An approval names the state hash it was granted against. When the
store moved from `726dc355` to `9d60fa65`, the approval for the first state was refused as stale and
nothing was written. A signature moved onto a different diff is refused. An approval minted by the
issuing service itself is refused. A valid signature from a different keypair is refused. The honest
path returns ALLOW with both signatures verified. An approval record therefore carries something a log
entry does not: this person authorised this exact effect, once, and cannot authorise it again by
accident.

**An agent cannot act on its own judgement.** The gate accepts a purpose only when it is `human_typed`
or drawn from a task record, and refuses `model`, `agent`, `llm`, `assistant` and `inferred`. "The agent
decided" is not a claim anyone can make about a permitted effect, because the write path has no branch
that produces it.

**You get the four questions that catch a governance system lying.** The most transferable product of
this work is a short list, and it came out of the failures. A quorum that counts rows rather than
distinct seats will certify one assent and one abstention as agreement. A verifier that checks a
signature and then discards it will write every row unsigned while reporting success. An audit that
does not know which verification contract a row used will report correct signatures as invalid. A
proposal path that never holds the payload bytes will accept bytes that do not hash to their own digest.
Three of those four were silences: the system reported clean. Anyone procuring a governance layer can
ask these four questions in an afternoon and learn more than a vendor questionnaire will tell them.

**The custody problem is solved without a server key.** Seat signatures use ML-DSA-87 (FIPS 204), the
level NSA requires for all classification levels under CNSA 2.0. The approving key never touches the
server, the server holds no copy of it, and when a rotation happened the server-side material was
destroyed and the fingerprint recorded instead. For records that must stay verifiable for decades, or
for work that will be assessed against CNSA 2.0, that is the difference between a plan and a deployed
path.

**Numbers, not adjectives.** 930, 667 and 469 vote rows audited on three independent boxes with zero
referential violations. Five fault types, each proven able to fail and then restored to a clean
baseline. A measured false-positive rate on held-out corpora rather than a claimed one. Most safety
claims arrive without a denominator. This one carries its denominators, including the rows it could not
reach.

**What it costs.** An adopter must run a signer off the server, hold their own keys, and accept that
every write passes a gate that can say no. That friction is the mechanism, not an implementation
detail: a gate that cannot refuse is a formality, and the refusal is what makes the receipt worth
anything. The operational price is one extra step per approved action and one key ceremony per seat.

**What it is not.** It is not a safe model, and no adopter should read it as one. It bounds what a model
can cause without a person, and it makes every permitted cause checkable. That is narrower than safety,
and it is more useful than assurance.

## 3. The journey

### 3.1 Leg one: containment

The first build put a model inside a cage and asked whether the cage held. The immediate discovery was
that the question is unanswerable as posed: a model asserting its own compliance is evidence of nothing.
What replaced it was a falsifier cadence — a weekly battery of adversarial probes, each producing one of
four outcomes: PASS, FLAGGED, NOT_CHECKED, or held.

The most important of those is NOT_CHECKED. In the most recent complete week the cadence recorded 7
probes run, 3 PASS, 4 NOT_CHECKED, 0 FLAGGED. A program that reported 7 of 7 would have been lying by
aggregation: four of those probes had no measurement behind them, and the honest report says so. This
habit — NOT_CHECKED as a first-class outcome, never folded into a pass rate — is the thing that
eventually made the gate's defects findable.

### 3.2 Leg two: grounding

The second leg attacked a different failure: a fluent reply that cites nothing real. A grounding check
was built that returns GROUNDED only when a claim resolves to a hashed artifact with a matching span,
and refuses a claim that cites model output as its own source. It refuses a negated span, so a reply
claiming "267x" is not grounded by a document saying "this is not 267x". It flips to TAMPERED when the
receipt count is altered.

Two measured corpora followed, and both numbers are small and should be read as such:

| Corpus | Cases | False positives | False negatives |
|---|---|---|---|
| A, general claims | 20 | 10.0% (2/20) | 5.0% (1/20) |
| B, after negation fix | 20 | 5.0% (1/20) | 5.0% (1/20) |
| C, citation-specific | 41 | 5.0% (2/41) | 14.3% (6/41) |

Both false positives in corpus A traced to one cause: the negation matcher treated the words "refused"
and "never" as negating what followed. The single false negative was a byte-identical duplicate of a
true case, a mislabel left uncorrected after seeing results. Fixing the matcher converted corpus A into
a development set, which is why corpus B exists and why neither number may be quoted as a held-out rate.

Corpus C then found a hole the negation fix had not closed: a citation denial *after* the cited name
("The Ramirez study was not published anywhere") still counted as anchoring. The fix was a narrow
forward clause reader. That fix is a phrase list, and its accuracy against denial wording not on the
list is unmeasured. This is stated here rather than in a footnote because it is the characteristic
failure mode of the whole program: each fix closes the case that found it and leaves an adjacent case
unmeasured.

### 3.3 Leg three: intent

The third leg addressed a gap that grounding cannot: a true statement can still be an unauthorized
change. Approvals were bound to a computed effect and a state hash, and the purpose field accepts only
human-typed text or a task record, never a model's inference. The issuer was changed so it cannot mint
an approval; it returns bytes to sign and nothing else. Signing is ML-DSA-87 against a key the server
never holds.

The mechanism was then measured in both directions. An honest approval returned ALLOW with both
signatures verified. Each of six forgeries was refused: a signature moved to a different diff, an
edited approver name, the retired HMAC signature, a valid ML-DSA-87 signature from a different keypair,
an approval minted by the application's own issuer, and a proposal carrying an unknown key at its root.

The property that makes this leg more than a signature check is that an approval buys exactly one state.
After a guarded write landed, an independent fresh read hashed the table and confirmed the write's own
predicted post-state, which permanently staled the approval used to make it. A replay against the same
approval is refused as stale, not re-executed. Updates and creates were each proven end to end twice.
The delete path was the last to land, on 2026-11-20: approval A-6c9c473a1e7d05a5 over grant
G-e729eac87e41065a removed one throwaway row, the writer reported WRITTEN_AND_VERIFIED, and an independent
fresh read hashed the table to 823b6ecb against the 823b6ecb the guard predicted before the write. All
three write paths now share one property: the approval names a state hash, and the write is refused if the
store is not in that state.

### 3.4 Leg four: the gate

The fourth leg is the subject of the rest of this paper. It answers one question with a
machine-checkable answer: *did a required set of distinct principals attest to these exact bytes?*

Four parts: a crossing (a proposed change with a payload and a digest), an escrow of the payload bytes,
a quorum of independently signed seat votes, and an audit that recomputes the relation from stored state
rather than trusting the write path. Signatures are ML-DSA-87 (FIPS 204). Three independent
deployments, each with its own store, its own functions, and its own audit lineage.

## 4. Mechanism

**Crossing and escrow.** A crossing records a payload, a digest over it, a proposing seat, and an
epoch. The digest is the crossing's identity. Payload bytes are escrowed at submission and the
submission is refused (HTTP 400, no proposal created) if the bytes do not hash to the digest. A proposer
who declines to supply bytes records `missing_at_submission`, so the absence is visible. Escrow holds
structural or synthetic content only; a payload that cannot be expressed structurally is not escrowed
and the crossing is recorded as declined.

**Quorum.** Each seat signs `CONCLAVE-VOTE-V2|proposal_id|seat_digest|voter_node_id`. The gate counts
authenticated distinct seats. Abstentions are not consent. A duplicate row for a seat that has already
voted cannot add to the count; the newest row per seat wins. A row whose signature does not verify is
not counted, so a row written directly into the store cannot complete a quorum.

**Audit.** An independent function recomputes the relation: every vote row must resolve to a seat, a
key, a valid signature over its own recorded values, and a proposal. It is written to fail loudly, and
it is required to be provably able to fail.

**Closure.** Crossings bind into a Merkle root per epoch. An epoch closes by re-pinning a root against a
matching root. Journal rows are never deleted to make a root match.

## 5. Threat model

In scope: row injection by an attacker with store write access; duplicate-seat inflation;
abstention-as-consent; payload substitution after the fact; vote-value tampering; orphan and dangling
references; silent escrow absence.

Out of scope: compromise of the keystore holding all seat keys; compromise of the audit function
itself; and any claim that a quorum means a change was desirable.

## 6. Method

A five-arm battery per deployment, run in two directions. Each arm must be shown able to fail: the
forged condition must be rejected *and* the honest condition must still succeed. A fix with only the
first direction is not a fix, because it can be satisfied by a gate that refuses everything.

| Arm | Injected condition | Required outcome |
|---|---|---|
| solo_seat | one assent | `pending` |
| abstention | one assent + one abstention | `pending` |
| dup_seat | one assent + a duplicate row for the same seat | `pending` |
| escrow | payload not hashing to its digest | refused 400, no proposal |
| determinism | honest assent from two distinct seats | `agreed`, identical across passes |

Exit required every arm green twice consecutively, escrow enabled, distinct payload content per run,
and identical arm outcomes across passes. Separately, each audit had to pass a five-type fault matrix —
tamper, duplicate seat, orphan row, hash substitution, unescrowed bytes — each producing a violation and
each returning to clean after restore.

## 7. Results

### 7.1 Arms, before and after repair

| Box | Before | After | Passes |
|---|---|---|---|
| C1 | 2 of 5 green | 5 of 5, identical | two consecutive |
| C2 | arms green, audit red (24 unsigned rows) | 5 of 5, identical | two consecutive |
| C3 | 3 of 5; gate accepted a forged quorum | 5 of 5, identical | two consecutive |

C2's before-column is the instructive one. The arms passed while the audit failed, because the arms
tested the gate and the audit tested the store. A gate that does not require authenticity passes a
battery that only asks whether forged *counts* are rejected.

### 7.2 Referential audits at close

| Box | Vote rows | Signed-verified | Legacy unsigned | Uncast | Violations |
|---|---|---|---|---|---|
| C1 | 930 | 475 | 268 | 181 | 0 |
| C2 | 667 | 491 (V1 469, V2 22) | 94 | 68 | 0 |
| C3 | — | 469 | — | — | 0 |

Twelve rows across C2 and C3 carry a disclosed disposition rather than a pass: unsigned votes written
during a window in which the store's schema carried none of the provenance fields, so the signature was
destroyed by storage rather than declined by the seat. They are retained as evidence of the regression
window, never counted as attestation, and the epochs they belong to are recorded as uncertified.

### 7.3 Content audits and the unverifiable corpus

| Box | Rows held | Verified | Unverifiable from the ledger alone |
|---|---|---|---|
| C1 | 235 | 235 / 338 | 103 |
| C2 | 235 | 228 / 282 | 54 |
| C3 | 233 | 225 / 310 | 85 |

A clean referential count and an unverifiable-corpus count are reported together or not at all. The
unverifiable rows are crossings made before escrow existed: their digests are recorded, their bytes are
not, so nobody can now demonstrate what they carried. They are not violations. They are permanently
weaker evidence, and an artifact quoting only the row count is misleading.

### 7.4 Fault matrix

All five fault types produced a violation on all three deployments and returned to exact baseline after
restore. Representative: an orphan journal row moved C2 from 240 to 241 rows, held 235 to 236, findings
7 to 9. A hash substitution moved verified 228 to 227 and unverifiable 54 to 55 with a new
`escrow_content_mismatch`. A single vote value flipped from assent to dissent took C1 from `ok: true` to
`ok: false` with one violation naming the row and the seat, and back to `ok: true` on restore.

## 8. The four defect classes

**D1 — Counting rows instead of seats, and not reading the value.** The quorum read a vote table and
counted rows. It did not check the vote value, so an abstention contributed to assent. It did not
deduplicate by seat, so one seat writing twice reached a two-vote threshold. It was not broken in the
obvious direction: one assent alone correctly stayed pending, which is exactly why it survived review.

**D2 — Verifying a signature and then discarding it.** The vote function verified the caller's
signature, then wrote a row with `voter_signature` present and empty. Every row it wrote was unsigned.
This is the serious one. The gate was not miscounting; it was accepting rows it had never
authenticated, and the store recorded the absence in a field that looked populated by name.

**D3 — A row that was not self-describing.** The audit selects a verification contract by checking
whether a field is present. The vote function never wrote that field, so the audit fell back to the
older contract and reported 24 correct signatures as invalid. The signature was right; the row was
incomplete. A contract selected by the absence of a field fails toward rejection, which is safe, and
toward a false alarm, which is not free.

**D4 — A proposal path that never held the bytes.** The digest was recorded; the bytes were not. A
payload that did not hash to its own digest was accepted. The crossing could be asserted and never
examined.

Each was found by running the battery, not by reading the code. Each was repaired with the failing
evidence, the layer named, the change, and a re-run proving both directions.

**The meta-observation, which is the paper's thesis.** Three of the four were silences: a field that
exists and is empty, a contract selected by a missing field, an escrow that was configured and off for
eleven days. Silent failure in a verification path is worse than loud failure, because the green count
is the thing a reader trusts. The only reason these were found is that the system was built to produce
NOT_CHECKED and to be run against itself.

## 9. What the journey establishes

Section 2 stated the purchase. This section states the claim behind it, which is narrower.

Not that the AI is safe. That the system around it can be shown wrong, and that it has been, four times,
by its own instruments, with each falsification turned into a test that would catch its recurrence.

The transferable claim is about reporting. A gate that reports `ok: true` over the part of the corpus
it could reach, without saying what it could not reach, is indistinguishable from a gate that checked
everything. The same is true of a monitor that reports a pass rate without its NOT_CHECKED count, a
grounding check that quotes a false-positive rate from a corpus it has since trained on, and a quorum
that reports agreement without saying whether the seats were independent.

## 10. Related work

Components, all predating this work: Merkle-bound append-only logs (Laurie, Langley and Kasper, RFC
6962, June 2013, superseded by RFC 9162); the Byzantine generals formulation of quorum agreement
(Lamport, Shostak and Pease, 1982); certified digital signatures (Merkle, 1979); timestamping (RFC
3161); and the post-quantum signature standard ML-DSA (NIST FIPS 204, 2024), with ML-DSA-87 the
parameter set required by NSA's CNSA 2.0 for national-security systems.

Adjacent in method rather than in mechanism: shielding for learned policies, which interposes a
verified safety layer between a policy's proposal and its effect (Alshiekh et al., AAAI 2018, pp.
2669–2678); and the AI-control programme, which measures whether a monitor catches a deliberately
misbehaving model rather than assuming it would (Greenblatt, Shlegeris and Roger, arXiv:2312.06942,
2023). Both share this paper's premise that a system's safety claim is only as good as the measurement
that could have refuted it.

What we have not seen combined in one measured artifact, and therefore claim: a crossing gate whose
quorum requires distinct post-quantum seat signatures over the recorded bytes, whose payloads are
escrowed so a past crossing can be shown wrong, whose audit is proven able to fail in five distinct
ways on three independent deployments, and whose unverifiable history is counted and disclosed
alongside its clean counts.

**Not claimed:** primacy. A search for prior art in this area surfaced work whose titles I could not
verify against a retrievable source, and unverifiable citations have been removed rather than included
on trust. The honest positioning is *different in kind in one respect*: the artifact states what it
cannot verify, in the same sentence as what it can.

## 11. Limits

1. **Single custodian.** All three seat private keys are held in one workspace keystore. The correct
   description of a 2-of-3 crossing here is: one operator drove three seat identities over the same
   bytes. It is not independent multi-party agreement, and no artifact produced from this work says
   otherwise.
2. **V2 does not bind the vote value.** The message covers the payload and the seat, not the assent or
   dissent. 22 rows on C2 carry a vote value not covered by their signature. V1 binds it. Closing this
   needs a V3 message and a coordinated epoch-cycle change.
3. **The audit's escalation path has a gap.** On one deployment the alert block runs before the vote
   loop, so vote-level violations return no alert id and do not escalate. The audit still reports them;
   the alert channel does not carry them.
4. **Consensus is not truth.** A crossing agreed by 2 of 3 seats is agreed, hash-identical, and nothing
   more.
5. **The fault matrix is a development set.** Its five types are now known to the implementation. The
   rate at which the audit catches unanticipated faults is not measured.
6. **The approval gate is proven, but its grant issuer is crude.** Update, create and delete are each
   executed and verified end to end. The issuer still demands a non-empty field list that the guard
   ignores for deletes, so a delete can only be prepared by naming a field that has no effect. That is a
   wart in the permission layer, not in the verification layer, and it is recorded rather than smoothed.
7. **Corpus sizes are small.** Twenty, twenty, forty-one. Percentages from these denominators are
   indicative, not estimable rates, and no confidence interval is claimed.
8. **One leg is inert.** A control parameter used to inject an absent digest is honoured by one
   deployment's content instrument and silently ignored by the other two.
9. **The citation matcher is a phrase list**, and its accuracy against wording not on the list is
   unmeasured.

## 12. Reproduction

Three independent deployments, each with its own store, function set and audit lineage. The battery was
token-gated, hard-expiring, and disabled after use, with its token destroyed. Audit verdicts are
recomputable from stored rows alone, which is the property that lets a third party check the numbers
rather than trust them.

## 13. What would falsify this

- A forged quorum completing on any deployment: two rows for the same seat, an abstention counted as
  assent, or an unsigned row counted, any of which reaching `agreed`.
- A crossing whose stored bytes do not hash to its digest, accepted.
- A fault of any of the five matrix types leaving the audit `ok: true`.
- A vote row signed by a key other than its seat's registered key, counted toward quorum.
- A re-pin of a closure root against a non-matching root, or a journal row deleted to make a root match.
- A grounding verdict of GROUNDED for a claim with no matching span in a hashed artifact.
- An approval executed twice, or executed against a state other than the one it named.

Any one of these, reproduced, invalidates the corresponding claim.

---

## Appendix A — Defect ledger

| ID | Deployment | Defect | Evidence | Both directions proven |
|---|---|---|---|---|
| D1 | C1 | Quorum counted rows; value unread; no seat dedup | agree+abstain → `agreed`; agree+dup → `agreed` | forged → `pending`; honest → `agreed` |
| D2 | C1, C2 | Signature verified then discarded | `voter_signature` length 0 on every written row | rows now carry 9,254-char signature + key id |
| D3 | C2 | `seat_digest` never written; audit fell back to V1 | 24 `vote_signature_invalid` on valid V2 signatures | `verified_format` V2 = 22; 0 invalid |
| D4 | C1 | `submitProposal` held no bytes | mismatched digest accepted | refused 400, no proposal created |
| D5 | C2 | Escrow configured and off since 2026-11-08 | deployed code diverged from every local copy | escrow passes; mismatch refused |
| D6 | C3 | Gate counted rows; accepted unsigned rows | forged quorum of two C1 rows, no C2 vote → `approved` | same injection → `pending`; honest → `approved` |

## Appendix B — Errors made during the work

Recorded because a paper reporting only its findings overstates its own method.

1. An authenticity check was first written to resolve keys from the node table only. It rejected every
   real vote and no proposal could reach agreement. Corrected to registry-first resolution by recorded
   key id, mirroring the audit.
2. The battery was run against a deployment whose vote function discarded signatures, and the audit was
   not re-checked afterwards. That wrote 84 unsigned rows on one box and 24 on another and reddened both
   audits. A condition was reported met before that check existed; the claim is supported only after the
   repair.
3. A first reading of a three-way vote classifier treated non-assent values as uncast, hiding a real
   tamper. Corrected; the tamper then produced a violation.
4. A builder edit was diagnosed as a platform failure when the real cause was a standing deployment
   freeze on that application. The misdiagnosis was retracted.
5. Fixtures created by the battery were removed by bounded, explicit id windows, never by broad delete.
   Historical rows, dispositioned rows and the pre-signing defect rows were not touched.

## Appendix C — Citation sweep, run 2026-11-20

| Source | Status |
|---|---|
| RFC 6962, Certificate Transparency, June 2013 | Verified. **Obsolete**; superseded by RFC 9162. Cited as history. |
| RFC 9162 | Verified as the current successor by RFC 6962's own status header. |
| Greenblatt, Shlegeris, Roger, arXiv:2312.06942, 2023 | Verified: arXiv DOI 10.48550/arXiv.2312.06942, ACM DL entry. |
| Alshiekh et al., AAAI 2018, pp. 2669–2678 | Verified via multiple independent citing papers. |
| NIST FIPS 204, ML-DSA, 2024 | Verified as the standard; parameter set ML-DSA-87 in use throughout. |
| NSA CNSA 2.0 | Verified as the requirement source for ML-DSA-87. |
| Lamport, Shostak, Pease, 1982 | Standard reference, not independently re-fetched in this sweep. |
| Merkle, 1979; RFC 3161 | Standard references, not independently re-fetched in this sweep. |
| "Beyond Approved Actions" (runtime action validation) | **Not verified.** No retrievable source located. Removed from the bibliography rather than cited on trust. |

Remaining pre-publication gates:

- [x] Citation sweep run; unverifiable entry removed.
- [x] Limit 2 (V2 unbound vote value) moved into the abstract, 2026-11-20.
- [x] Limit 6 resolved: delete leg executed and verified 2026-11-20 (WRITTEN_AND_VERIFIED, post-state 823b6ecb).
- [x] Two-key curation: Gabriel vetting complete; Leon approval recorded 2026-11-20 21:12 CT.
- [x] Publication scan: personal-data-guard exit 0, one WARN (clinical word, no value).
- [x] Custody sentence present in the abstract, section 1 and section 10.
