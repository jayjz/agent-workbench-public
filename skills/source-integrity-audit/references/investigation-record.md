# Investigation record (optional)

Use this when the investigation involves multiple claims or overlapping source chains. Preserve unknowns instead of inventing values.

## Source entry
- Source ID:
- Canonical URL / DOI / record ID / repo path at commit:
- Title and original responsible party:
- Published / modified / accessed (distinguish dates; unknown if not established):
- Type: artifact | primary document | study | dataset | secondary analysis | aggregator | model summary | other
- Inspected exact location (page/line/verse/timestamp/table):
- Exact observation or narrowly paraphrased passage:
- Original available? yes | no | unresolved
- Access or preservation limitation:
- Provenance family ID:
- Upstream dependency: source ID + link evidence + VERIFIED | INFERRED | UNKNOWN

## Claim entry
- Claim ID and atomic formulation:
- Materiality:
- Repository/report location:
- Citing source IDs, with DIRECT | CONTEXT | MISATTRIBUTED | UNCHECKED:
- Independent provenance families: [IDs] (do not count unchecked independence)
- Best direct evidence and precise location:
- Most serious counterevidence and precise location:
- Alternative explanation:
- Evidence state: SUPPORTED | INFERRED | UNRESOLVED | CONFLICTED
- Disposition: KEEP | QUALIFY | RESEARCH | REMOVE
- Next discriminating check:

## Lineage notation
`S1 → S2` means S2 derives from S1, **not** that S2 independently corroborates S1.
Annotate each edge `[VERIFIED: quoted primary record]`, `[INFERRED: matching material]`, or `[UNKNOWN]`.
Do not describe two sources as independent solely because their websites, publishers, or authors differ.

## Adversarial checks
For each high-impact claim, ask:
- Could all the citations trace to one artifact, translation, dataset, or publicity statement?
- Is an author citing themselves, a circular chain, a correction, or a superseded version?
- What would a careful opponent cite against this claim?
- Does the source actually prove the claim, or only a narrower/background fact?
- Are event, document creation, publication and retrieval dates conflated?
- Would independent measurements or alternate translations change the outcome?
- Which missing record would most efficiently distinguish competing explanations?

## Report and reproducibility
Record date, tool/access constraints, repository branch/commit, specific searches and inspected originals. Report inaccessible materials explicitly. Do not include personal data unnecessarily or download material beyond authorization.

## Methodology references (guidance, not automatic authority)
- W3C PROV Overview: https://www.w3.org/TR/prov-overview/
- OpenAI skill authoring and progressive disclosure: https://learn.chatgpt.com/docs/build-skills
- Berkeley Protocol on Digital Open Source Investigations (OHCHR): https://www.ohchr.org/en/publications/policy-and-methodological-publications/berkeley-protocol-digital-open-source
