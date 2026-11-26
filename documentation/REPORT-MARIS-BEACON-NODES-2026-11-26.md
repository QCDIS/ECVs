# MARIS Beacon node survey: chat record (2026-11-26)

Side session started from the ECVs workflow session. Read-only: no repository
file edited, nothing committed. The full node table is also saved as
`maris-beacon-nodes.md` in the notes folder
`side-session-notes\local_ff85f0e0-d949-4d2a-a4d9-f7d3de90816b`.

## 1. Task

List the Beacon data nodes that MARIS publishes and describe each one, to see
which other research infrastructures the ECVs workflow (`conf_ri_registry` in
`DEMO-Files/vre-private/user/test-virtual-lab-1/ECVs/scripts/make_notebook.py`)
could add. Call only `GET /api/health`, `/api/info` and `/api/tables`, with no
token, and at most one small `/api/table-schema` per node.

The workflow already knew three nodes: `beacon-iriscc` (ACTRIS, IAGOS),
`beacon-argo` (query planning error on 2026-11-25) and `beacon-cdi` (401).

## 2. How the node list was found

- The docs page
  https://maris-development.github.io/beacon/available-nodes/available-nodes.html
  gives a URL for only one node, `beacon-wod.maris.nl`, which is open. It
  describes Euro-Argo, WOD and CMEMS CORA nodes run for Blue-Cloud2026 and
  FAIR-EASE that need a token, but their URLs appear only after you sign up
  for "BC2026 Beacon Beta Access" (ask info@maris.nl).
- The official machine-readable list of public nodes, used by Beacon Studio,
  is at https://beacon-datalake.org/api/studio/public-nodes. It lists WOD, ERA5
  and ARGO. `beacon.maris.nl` redirects to beacon-datalake.org.
- The other hostnames come from example notebooks on GitHub:
  maris-development/beacon-blue-cloud, maris-development/beacon-poc-rws,
  gher-uliege/DIVAnd-FAIR-EASE and fair-ease/py-udal-fe-impl.
- `beacon-iriscc` is in no MARIS list found; it is known from QCDIS/ECVs.

## 3. Result

| Node URL | Research infrastructure / domain | Reachable | Beacon | Token | Tables | Notes |
|---|---|---|---|---|---|---|
| beacon-wod.maris.nl | NOAA World Ocean Database (ocean profiles) | yes | 2.0.2 | no | `easy-wod`, `default` | Official open demo node, rate-limited |
| beacon-era5.maris.nl | Copernicus ERA5 daily statistics (2 m temperature, precipitation, 1950-2025) | yes | 1.5.4 | no | `era5_daily_mean/max_2m_temperature`, `era5_daily_total_precipitation`, `daily`, `daily_single_levels`, `daily_pressure_levels`, `default` | In the public list; a demo, not a copy of the Copernicus data store |
| beacon-argo.maris.nl | Euro-Argo / Argo floats, core and BGC | yes | 2.0.2 | no | `argo`, `argo_core`, `argo_bgc`, `easy_one_argo`, `easy_one_argo_bgc`, `default` | Now open. No data query sent, so the 2026-11-25 query error is not re-checked |
| beacon-iriscc.maris.nl | IRISCC: ACTRIS, IAGOS, plus air-quality and temperature grids | yes | 1.6.0 | no | `actris`, `actris-in-situ`, `actris-nrt`, `iagos-l1`, `iagos-l2`, `no2`, `o3`, `pm10`, `pm2_5`, `annual_mean_black_carbon`, five temperature tables, `default` | No ICOS table; the `pm10` schema is a grid (x, y, year) |
| beacon-ihm.maris.nl | Rijkswaterstaat North Sea / Wadden Sea monitoring (benthos, fish, birds, chemistry, plankton, bathymetry, wind farms) | yes | 2.0.2 | no | 97 tables (`ihm_*`, `mon_*`, `prj_*`, `use_wind_*`, `aquadesk2026`, ...) | Not in the public list, but open when probed |
| beacon-cdi.maris.nl | SeaDataNet CDI (European marine data) | yes | ? | yes | ? | 401 |
| beacon-cdi-incremental.maris.nl | SeaDataNet CDI, incremental updates | yes | ? | yes | ? | 401 |
| beacon-cdi-ts.maris.nl | SeaDataNet CDI, temperature/salinity | no | ? | ? | ? | 502 on all three endpoints |
| beacon-cmems.maris.nl | Copernicus Marine (CMEMS) in-situ, including BGC | yes | ? | yes | ? | 401 |
| beacon-cora-pr.maris.nl | CMEMS CORA profiles | yes | ? | yes | ? | 401 |
| beacon-cora-ts.maris.nl | CMEMS CORA time series | yes | ? | yes | ? | 401 |
| beacon-emod-chem.maris.nl | EMODnet Chemistry | yes | ? | yes | ? | 401 |
| beacon-wb1-ts.maris.nl | Blue-Cloud WorkBench 1: merged temperature/salinity | yes | ? | yes | ? | 401 |
| beacon-wb2-eutrophication.maris.nl | Blue-Cloud WorkBench 2: merged eutrophication | yes | ? | yes | ? | 401 |

Also found:
- Mirrors outside maris.nl, not probed: `beacon-{argo,wod,cora-pr,cora-ts,seadatanet,emodnet-chemistry,wb1-ts}.d4science.org`
  and `beacon-argo.eoscfe.mesocentre.uca.fr`.
- Guessed names `beacon-seadatanet`, `beacon-emodnet-chemistry` and
  `beacon-icos` at maris.nl time out, so no such nodes appear to exist.

## 4. Candidates for the ECVs workflow (no token needed)

- **ERA5:** surface temperature and precipitation.
- **WOD:** ocean temperature, salinity and oxygen.
- **Argo:** now open; ocean temperature/salinity and BGC variables (O2,
  nitrate, chlorophyll, pH), if the query error is gone.
- **IRISCC grids:** NO2, O3, PM10/PM2.5, black carbon.
- **IHM:** Dutch coastal biology and chemistry, for biodiversity variables.

CMEMS, CORA, EMODnet Chemistry, SeaDataNet CDI and the Blue-Cloud WorkBench
nodes need a Blue-Cloud2026 Beacon Beta token.

## 5. Q&A: what is IRISCC?

IRISCC stands for Integrated Research Infrastructure Services for Climate
Change risks. It is a Horizon Europe project that started in 2024 and should
run for about four years. It brings European environmental and climate
research infrastructures together into one set of services for research on
climate-change risks: hazards, exposure, vulnerability and adaptation.
Members include ACTRIS (aerosols, clouds, trace gases), IAGOS (instruments on
commercial aircraft), ICOS (greenhouse gases), eLTER (long-term ecosystem
research) and others from the ENVRI cluster. It offers access to facilities
and data and builds common, interoperable data services.

MARIS takes part as a data-service provider. `beacon-iriscc.maris.nl` is the
project's Beacon node, one query point for data from several IRISCC
infrastructures, which is why it mixes ACTRIS tables, IAGOS tables and gridded
air-quality and temperature layers. ICOS is a member, which is likely why the
QCDIS/ECVs README lists it with this node, but the node had no ICOS table on
2026-11-26.

This answer came from general knowledge, not a lookup. Check the coordinator
and the full member list on the project's own site before relying on them.
