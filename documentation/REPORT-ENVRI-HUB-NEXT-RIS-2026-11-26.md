# ENVRI-Hub NEXT: research infrastructures (survey 2026-11-26)

Read-only web survey for the ECVs workflow ([REPORT-WORKFLOW-ECVS-2026-11-25.md](../../../../../docs/reports/REPORT-WORKFLOW-ECVS-2026-11-25.md)). Nothing was downloaded.
Project: ENVRI-Hub NEXT, Horizon Europe HORIZON-RIA, grant 101131141,
1 Feb 2024 - 31 Jan 2027, EU contribution EUR 5 M, coordinator EGI Foundation
(Stichting EGI, NL). [S1][S3]

## How many RIs? Sources disagree

- **CORDIS objective [S1]** names 8: "key ESFRI Landmarks (ACTRIS, AnaEE ERIC,
  EPOS ERIC, EuroArgo ERIC, IAGOS AISBL, ICOS ERIC, LifeWatch ERIC) and ESFRI
  Projects (eLTER)". It also names SeaDataNet as "the marine data
  infrastructure" among the support providers, not as an RI.
- **envri.eu project page [S2] and EGI project page [S3]** both say "ENVRI-Hub
  NEXT brings together 11 Research Infrastructures representing 4 Earth system
  domains": the 8 above plus **Data Terra, SeaDataNet, SIOS**. EGI calls Data
  Terra "a research E-Infrastructure".
- Only **EPOS ERIC, Euro-Argo ERIC, ICOS ERIC, LifeWatch ERIC** are formal
  beneficiaries (CORDIS participant list [S1], envri.eu partner list [S2]).
  ACTRIS, AnaEE, IAGOS, eLTER, SIOS, SeaDataNet and Data Terra are not
  beneficiaries in their own name; they take part through member institutes
  that are partners (e.g. CNRS, NILU, FZJ, FMI, Ifremer, UFZ, CNR, MARIS).
  Which institute represents which RI is not stated on any page read, so it is
  not filled in below.

## RI table

Columns: Role = role in ENVRI-Hub NEXT per [S1]/[S2]/[S3]; Hub portal = listed
on the ENVRI-Hub "Data Portals" page [S4]; Beacon = on a MARIS Beacon node, per
a read-only probe of the MARIS Beacon nodes on 2026-11-26 (`/api/health`, `/api/info`, `/api/tables`, no token).

| RI (acronym) | Subdomain | ESFRI status | Legal form | Role in ENVRI-Hub NEXT | Main data portal | MARIS Beacon |
| --- | --- | --- | --- | --- | --- | --- |
| Aerosol, Clouds and Trace Gases Research Infrastructure (ACTRIS) | Atmosphere | Landmark [S1] | ERIC (ACTRIS ERIC, 2023) [K] | Named RI [S1][S2][S3]; not a beneficiary; Hub data portal [S4] | https://data.actris.eu/ [S4]; ACTRIS homepage links https://dc.actris.nilu.no/ [S5] | **Yes**: `actris`, `actris-in-situ`, `actris-nrt` on beacon-iriscc (open) |
| In-service Aircraft for a Global Observing System (IAGOS) | Atmosphere | Landmark [S1] | AISBL [S1][S5] | Named RI; not a beneficiary; Hub data portal and "FAIR ENVRI Atmospheric Data Demonstrator" [S4] | https://iagos.aeris-data.fr/ [S4][S5] | **Yes**: `iagos-l1`, `iagos-l2` on beacon-iriscc (open) |
| Integrated Carbon Observation System (ICOS) | Atmosphere / cross-domain (atmosphere, ecosystem, ocean GHG) | Landmark [S1] | ERIC (2015) [S1 name; year K] | **Beneficiary** (FI), WP8 leader [S2]; Hub data portal and Carbon Footprint Tool [S4] | https://data.icos-cp.eu/portal/ [S4][S5] | **Not found**: no ICOS table on beacon-iriscc today, although the QCDIS/ECVs README names one |
| Svalbard Integrated Arctic Earth Observing System (SIOS) | Cross-domain (Arctic: atmosphere, ocean, cryosphere, land) | Not stated in sources read; ESFRI Landmark from background knowledge [K, unverified] | Not stated [S5] | Named RI [S2][S3] only; not a beneficiary; not on Hub data-portal page | https://sios-svalbard.org/metsis/search [S5] | No |
| Euro-Argo | Marine | Landmark [S1] | ERIC (2014) [S1 name; year K] | **Beneficiary** (FR) [S1][S2]; Hub data portal [S4] | https://www.euro-argo.eu/Argo-Data-access [S4] (RI site returned 503, unverified) | **Yes**: `argo`, `argo_core`, `argo_bgc`, `easy_one_argo(_bgc)` on beacon-argo (now open, metadata only tested) |
| SeaDataNet (Pan-European infrastructure for ocean and marine data management) | Marine | Not on ESFRI roadmap [K] | No legal entity; network of national data centres [K] | Named RI [S2][S3]; CORDIS calls it "the marine data infrastructure" (support provider) [S1]; MARIS BV (its technical coordinator [K]) is a beneficiary; Hub portal as "Marine Data Infrastructure" [S4] | https://cdi.seadatanet.org/search [S4] (site 503, unverified) | **Yes, token**: beacon-cdi, beacon-cdi-incremental (401); beacon-cdi-ts (502) |
| European Plate Observing System (EPOS) | Solid Earth | Landmark [S1] | ERIC (30 Oct 2018) [S5] | **Beneficiary** (IT), WP7 leader "Data and Services Catalogue" [S2]; INGV is its linked third party [S1]; listed (no link) on Hub portal page [S4] | EPOS Data Portal, linked as `/dataportal` on https://www.epos-eu.org/ [S5] | No |
| Analysis and Experimentation on Ecosystems (AnaEE) | Biodiversity / ecosystems | Landmark [S1] | ERIC [S1][S5] (2019 [K]) | Named RI; not a beneficiary; Hub portal page links its homepage [S4] | No single data portal; facility catalogue https://isia.cnrs.fr/catalog/1/services [S5] | No |
| Integrated European Long-Term Ecosystem, critical zone and socio-ecological Research (eLTER RI) | Biodiversity / ecosystems | **Project** [S1]; "on the priority list" of the ESFRI Roadmap [S5] | Not stated (ERIC in preparation [K]) | Named RI; not a beneficiary; Hub data portal [S4] | Data Asset Register https://dar.elter-ri.eu/search [S4]; service portal https://www.elter-ri.eu/service-portal [S5] | No |
| LifeWatch (e-Science European Infrastructure for Biodiversity and Ecosystem Research) | Biodiversity / ecosystems | Landmark [S1] | ERIC (2017) [S2] | **Beneficiary** (ES) [S1][S2]; listed (no link) on Hub portal page [S4] | https://metadatacatalogue.lifewatch.eu ; https://search.lifewatch.eu [S5] | No |
| Data Terra | Cross-domain (French Earth-system data: AERIS atmosphere, ODATIS ocean, THEIA land surface, FormaTerre solid Earth, PNDB biodiversity) | Not on ESFRI roadmap; French national RI [S5][K] | Not stated [S5] | Named RI, described by EGI as "a research E-Infrastructure" [S3]; not a beneficiary | No single portal; per pole via https://www.data-terra.org/ [S5]. AERIS hosts the IAGOS portal. | No |

Legend: [K] = background knowledge, not confirmed on a page in this survey
(the ESFRI site returned HTTP 403, so no ESFRI status was checked there; the
Landmark/Project labels come from CORDIS [S1]).

Other Beacon tables vs ENVRI-Hub NEXT: `IRISCC` (beacon-iriscc's own name, and
its gridded no2/o3/pm/black-carbon/temperature layers) is **not** an ENVRI-Hub
NEXT RI; IRISCC is a separate Horizon Europe project (climate-change RI
services). WOD, ERA5, CMEMS/CORA, EMODnet Chemistry and Rijkswaterstaat IHM
nodes are not ENVRI-Hub NEXT RIs either.

## For the ECVs workflow

- In ENVRI-Hub NEXT **and** on an open Beacon node: ACTRIS, IAGOS (in use),
  Euro-Argo (beacon-argo, now open).
- In ENVRI-Hub NEXT, on Beacon but token-gated: SeaDataNet CDI.
- In ENVRI-Hub NEXT, not on Beacon (would need their own API): ICOS (Carbon
  Portal SPARQL/REST), EPOS, LifeWatch, eLTER (DAR), SIOS (METSIS), AnaEE,
  Data Terra poles.

## Non-RI partners (CORDIS [S1], envri.eu [S2])

Coordinator: EGI Foundation (Stichting EGI, NL).
- E-infrastructures / NRENs: CESNET (CZ), GRNET (GR); LIP (PT, linked third party).
- Universities: Universiteit van Amsterdam (NL; builds the ENVRI Knowledge Base),
  Lunds Universitet (SE).
- Research organisations: CNR (IT), CNRS (FR), CREA (IT), CSIC (ES, linked third
  party), INGV (IT, linked third party of EPOS ERIC), Forschungszentrum Jülich
  (DE), FMI (FI; EOSC Association liaison per [S1]), Ifremer (FR), NILU (NO),
  UFZ (DE).
- Company: MARIS BV (NL, SME).

CORDIS shows "Participants (20)" plus the coordinator, i.e. 21 organisations; it
does not say whether the coordinator is in the 20. envri.eu also counts 21.

## Open points

- The 8-vs-11 RI count: CORDIS (grant text) lists 8; the project's own pages
  list 11. Data Terra, SeaDataNet and SIOS are presumably contributing RIs/
  e-infrastructures added through member institutes; no page states that.
- No page labels any RI as a "data provider to the ENVRI-Hub catalogue". The
  Catalogue of Services (https://catalogue.envri.eu/) renders by JavaScript and
  could not be read; the Hub's About page shows "Contributing Research
  Infrastructures 0" (unfilled counter). [S4] data-portal listing is used as
  the best proxy.
- ERIC years for ICOS, Euro-Argo, AnaEE, ACTRIS, and SIOS's ESFRI status are from
  background knowledge, not checked against esfri.eu (403).

## Sources

- [S1] CORDIS, ENVRI-Hub NEXT, https://cordis.europa.eu/project/id/101131141 (objective, participant list)
- [S2] ENVRI community, project page, https://envri.eu/envri-hub-next/ (11 RIs, partners, WP leads)
- [S3] EGI, project page, https://egi.eu/project/envri-hub-next (11 RIs, coordinator, budget)
- [S4] ENVRI-Hub, https://envri-hub.envri.eu/data-portals and https://envri-hub.envri.eu/ (portals, demonstrators); also read catalogue.envri.eu, search.envri.eu/search/, /pages/about/
- [S5] RI homepages: actris.eu, iagos.org, icos-cp.eu, epos-eu.org, anaee.eu, elter-ri.eu, lifewatch.eu, sios-svalbard.org, data-terra.org. Failed: euro-argo.eu and seadatanet.org (503), esfri.eu (403), hub.envri.eu and kb.envri.eu (TLS errors).
- envri.eu/research-infrastructures/ (whole ENVRI community, "26 European Research Infrastructures"; no NEXT membership flags) — context only.
- MARIS Beacon node probe, 2026-11-26 (node list from beacon-datalake.org/public-nodes and the MARIS example notebooks), for the Beacon column.
