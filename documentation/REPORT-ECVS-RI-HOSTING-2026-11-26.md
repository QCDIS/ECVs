# Which research infrastructures host which ECVs (survey 2026-11-26)

This is a read-only web survey for the ECVs workflow (v2) in this folder. I read
web pages only: no dataset was downloaded, and no Beacon data query was sent. It
builds on two earlier reports in this folder:

- [REPORT-ENVRI-HUB-NEXT-RIS-2026-11-26.md](REPORT-ENVRI-HUB-NEXT-RIS-2026-11-26.md)
  covers the RIs themselves.
- [REPORT-MARIS-BEACON-NODES-2026-11-26.md](REPORT-MARIS-BEACON-NODES-2026-11-26.md)
  covers the Beacon nodes and their tables.

It also uses the workflow's own coverage run,
[results/coverage/ECVs-coverage.md](results/coverage/ECVs-coverage.md). That run
used the window lon 0-20, lat 45-55, 2024, 0-200 m, and found data for 11 of
the 55 ECVs.

## How to read this report

**Confidence of each RI-ECV link.** The tag is written after each RI in the tables:

| Tag | Meaning |
| --- | --- |
| **S** | The RI's own page or document states the ECV mapping. |
| **V** | A page states the variable, but the mapping to the ECV is mine (inferred). |
| **I** | Inferred from a platform or theme the page names, with no variable named. |
| **K** | Background knowledge only, not seen on any page in this survey. |

**Key finding on sources.** Only **SIOS** publishes a variable-to-GCOS-ECV
table (Core Data v1, Appendix 1) [R-SIOS]. None of the other RI websites read
(ACTRIS, ICOS, IAGOS, Euro-Argo, EMSO, SeaDataNet, JERICO, EMBRC, DANUBIUS,
eLTER, AnaEE, LifeWatch, EPOS) uses the words "ECV" or "EOV" on the pages
checked. Their ECV links are therefore V or I. There are a few secondary
statements:

- a UNFCCC SBSTA poster says ICOS is "based on the ECVs by GCOS";
- Petzold et al. (Tellus B 2015) says IAGOS covers the atmospheric-composition ECVs;
- a Copernicus in-situ use case says many ACTRIS variables are GCOS ECVs.

All three were seen only as search snippets.

**EXV codes.** I checked the codes against the NVS EXV collection
(`vocab.nerc.ac.uk/collection/EXV/current/`, fetched 2026-11-26).
EXV001-EXV055 are the 55 GCOS ECVs, in the GCOS order: atmosphere 001-016,
ocean 017-035, land 036-055. The collection now holds **69** concepts.
EXV056-EXV069 are GOOS biological and other EOVs that are not ECVs:

- phytoplankton, zooplankton, ocean bottom pressure, fish, sea turtles,
  seabirds, marine mammals, coral, seagrass, macroalgae, mangrove, microbes,
  benthic invertebrates, ocean sound.

The workflow's EXV loop stops at 055.

**GCOS names.** gcos.wmo.int shortens several NVS names [G1]:

| NVS name | gcos.wmo.int name |
| --- | --- |
| Cloud properties | Clouds |
| Aerosol properties | Aerosols |
| Ocean inorganic carbon | Inorganic Carbon |
| Marine habitat properties | Marine Habitats |
| Anthropogenic greenhouse gas fluxes | Anthropogenic Greenhouse Gas Emissions |

The NVS label for EXV043 has a typo ("Ice sheets ad ice shelves"). A GCOS
rationalisation of the ECV list (2024-25) proposes dropping the two
"Anthropogenic" ECVs [G4, snippet].

**Beacon column.** These values come from the Beacon report:

- **open** means the node answered without a token;
- **token** means the node returned 401;
- for token-gated nodes, the tables are unknown, so their ECV content is
  inferred from the node's described domain;
- `beacon-argo` is open now, but `conf_ri_registry` still marks it
  `token_required: True`, so the workflow skips it.

**Workflow column.** "Found" means the coverage run returned rows. "0 rows"
means a source matched but returned no data in the window. "-" means nothing
was found.

## Atmosphere (EXV001-EXV016)

| EXV | GCOS ECV | European RIs (variables; tag; source) | Global / Copernicus hosts | MARIS Beacon | Workflow |
| --- | --- | --- | --- | --- | --- |
| 001 | Surface pressure | ICOS atm. stations, pressure at sampling heights (V) [R-ICOS-A]; ACTRIS met at sites (V, coverage run); eLTER SOATM_027 meteo (V) [R-eLTER]; IAGOS aircraft pressure (V, coverage run) | C3S in-situ/ERA5 (K); ISPD, ICOADS (K) | ACTRIS, IAGOS on beacon-iriscc (open) | Found (ACTRIS, IAGOS) |
| 002 | Surface temperature | SIOS SCD 1.3 air temperature (**S**) [R-SIOS]; ICOS atm. meteo (V) [R-ICOS-A]; eLTER SOATM_027 (V); ACTRIS met (V) | GCOS: Berkeley Earth, HadCRUT/CRUTEM, GISTEMP, NOAAGlobalTemp, GHCN-D, ISD, HadISD [G2]; C3S (K) | ACTRIS, IAGOS (open); ERA5 T2m on beacon-era5 (open, not in registry); IRISCC temperature grids (open, not in registry) | Found |
| 003 | Surface wind speed and direction | SIOS SCD 1.1/1.2 (**S**); ICOS atm. meteo (V); eLTER SOATM_027 (V); ACTRIS met (V) | C3S/ERA5 (K); CMEMS Wind TAC [C4] | ACTRIS, IAGOS (open) | Found |
| 004 | Surface water vapour | SIOS SCD 1.8 humidity (**S**); ICOS atm. RH (V); eLTER SOATM_027 (V); EPOS-related GNSS IWV, "EPOS8" product at GFZ (I) [R-EPOS] | C3S water vapour [C2]; ESA CCI Water Vapour [C5]; HadISDH (K) | IAGOS H2O (open) | Found (IAGOS) |
| 005 | Precipitation | SIOS SCD 1.7 (**S**); eLTER SOATM_027 (V); ACTRIS met precipitation (V, coverage run) | GCOS: GPCC, CMAP, GHCN [G2]; C3S [C2] | ACTRIS (open, 0 rows); ERA5 daily precipitation on beacon-era5 (open, not in registry) | 0 rows |
| 006 | Surface radiation budget | SIOS SCD 1.4-1.6 net/SW/LW radiation (**S**); eLTER SOATM_028 radiation (V); ICOS ecosystem radiation components (K) | GCOS: BSRN/WRMC, WRDC [G2]; C3S [C2]; CAMS solar radiation service [C3] | - | - |
| 007 | Upper-air temperature | SIOS SCD 1.9 (**S**); IAGOS aircraft temperature (K for the page; the variable is in iagos-l2 per coverage run) | GCOS: IGRA, GRUAN, RATPAC, RAOBCORE/RICH [G2]; C3S/ERA5 (K) | IAGOS, ACTRIS (open) | Found (ACTRIS rows are surface) |
| 008 | Upper-air wind speed and direction | SIOS SCD 1.10/1.26 (**S**); IAGOS aircraft winds (K; in iagos-l2) | IGRA, GRUAN (K); C3S/ERA5 (K) | IAGOS (open) | Found |
| 009 | Upper-air water vapour | IAGOS ICH humidity, H2O in package 2d (V) [R-IAGOS]; ACTRIS FTIR/lidar water vapour (K); EPOS-related GNSS IWV (I) | GRUAN, IGRA (K); C3S [C2]; ESA CCI Water Vapour [C5] | IAGOS (open) | Found (IAGOS) |
| 010 | Earth radiation budget | none found | CERES (K); C3S [C2] | - | - |
| 011 | Cloud properties | ACTRIS Cloudnet (FMI): cloud classification, LWC/IWC (V) [R-ACTRIS]; IAGOS backscatter cloud probe (V) [R-IAGOS]; SIOS SCD 1.11/1.12 cloud type and base (**S**, mapped to WMO cloud entries) | ISCCP (K); C3S [C2]; ESA CCI Cloud [C5] | not in actris-in-situ; ACTRIS cloud remote sensing is not on Beacon (K) | - |
| 012 | Lightning | none found | WWLLN (K); no C3S/CAMS/CCI product [C1-C5] | - | - |
| 013 | CO2, CH4 and other GHGs | ICOS atm.: CO2, CH4 mandatory; N2O, CO, 222Rn, O2/N2 recommended (V) [R-ICOS-A]; IAGOS CO2, CH4 package 2d, data to WDCGG (V) [R-IAGOS]; ACTRIS FTIR (K); SIOS SCD 1.14/1.17 (**S**) | GCOS: WDCGG, NOAA GML, NDACC, TCCON [G2]; C3S, CAMS [C2][C3]; ESA CCI GHG [C5] | ACTRIS, IAGOS (open); no ICOS table on any node | Found (ACTRIS, IAGOS) |
| 014 | Ozone | ACTRIS in-situ O3, DIAL/FTIR O3 (V) [R-ACTRIS]; IAGOS O3 package 1 (V; ECV per Petzold, snippet) [R-IAGOS]; SIOS SCD 1.16 (**S**) | GCOS: WOUDC, NDACC, SHADOZ, NOAA GML [G2]; C3S, CAMS; ESA CCI Ozone | ACTRIS, IAGOS (open); IRISCC `o3` grid (open, not in registry) | Found |
| 015 | Precursors (aerosol, ozone) | ACTRIS NOx, VOCs (V) [R-ACTRIS]; IAGOS CO, NOx, NOy, NO2 (V) [R-IAGOS]; ICOS atm. CO (V); SIOS lists NO2 under GHG (**S**, misfiled) | WDCRG (K); CAMS reactive gases [C3]; ESA CCI Precursors [C5] | ACTRIS, IAGOS (open); IRISCC `no2` grid (open, not in registry) | Found |
| 016 | Aerosol properties | ACTRIS in situ (EBAS), lidar/photometer (ARES), with ~135 variables in total (V) [R-ACTRIS]; IAGOS aerosol package 2c (V); SIOS SCD 1.18-1.20 (**S**) | GCOS: WDCA, AERONET, MPLNET [G2]; C3S, CAMS; ESA CCI Aerosol | ACTRIS (open); IRISCC `pm10`, `pm2_5`, `annual_mean_black_carbon` grids (open, not in registry) | Found (ACTRIS) |

## Ocean (EXV017-EXV035)

Not one marine RI page read names ECVs or EOVs. The EMSO EGIM papers say the
module was built to support GOOS EOVs, and Blue-Cloud says JERICO feeds its EOV
workbenches [R-EMSO][R-JERICO]. Every ocean ECV has a matching GOOS EOV [G5].

| EXV | GCOS ECV | European RIs (variables; tag; source) | Global / Copernicus hosts | MARIS Beacon | Workflow |
| --- | --- | --- | --- | --- | --- |
| 017 | Sea-surface temperature | Euro-Argo, shallowest profile level (K) [R-ARGO]; SIOS SCD 4.4 (**S**); ICOS Ocean SST with fCO2 (K) [R-ICOS-O]; JERICO FerryBox/moorings T (V) [R-JERICO]; SeaDataNet CDI (V) [R-SDN] | GHRSST/OSTIA [G2]; C3S [C2]; CMEMS SST TAC [C4]; ESA CCI SST; EMODnet Physics [R-EMOD] | Argo (open; registry says token); WOD (open, not in registry); CDI, CMEMS, WB1 (token) | - (Argo, CDI skipped) |
| 018 | Subsurface temperature | Euro-Argo core T 0-2000 m, Deep 4000-6000 m (V) [R-ARGO]; EMSO EGIM T (V) [R-EMSO]; SIOS SCD 4.8 (**S**); JERICO gliders/CTD (V); SeaDataNet CDI and climatologies (V) | GTSPP, WOD, Coriolis, IQuOD [G2]; CMEMS INS TAC [C4]; EMODnet Physics | Argo (open); WOD `easy-wod` (open); CDI, CORA-PR, CMEMS, WB1 (token) | - |
| 019 | Sea-surface salinity | Euro-Argo (K); SIOS SCD 4.5 (**S**); ICOS Ocean SSS (K); JERICO (V); SeaDataNet (V) | GTSPP, CATDS/SMOS, PO.DAAC [G2]; CMEMS [C4]; ESA CCI SSS | Argo (open); WOD (open); CDI, CMEMS, WB1 (token) | - |
| 020 | Subsurface salinity | Euro-Argo core S (V); EMSO EGIM conductivity (V); JERICO (V); SeaDataNet (V) | GTSPP, WOD, Argo GDAC (K); CMEMS [C4] | Argo (open); WOD (open); CDI, CORA-PR, CMEMS, WB1 (token) | - |
| 021 | Surface currents | SIOS SCD 4.3 (**S**); JERICO HF radar (I) [R-JERICO] | Globcurrent, OSCAR [G2]; CMEMS [C4]; EMODnet Physics HF radar [R-EMOD] | CDI, CMEMS (token; inferred content) | - |
| 022 | Subsurface currents | Euro-Argo drift at ~1000 m (V) [R-ARGO]; EMSO ADCP/tilt current meters (V) [R-EMSO] | OceanSITES (K); CMEMS models (K); EMODnet Physics | CDI, CMEMS (token; inferred). Argo drift is trajectory data, not in the profile tables (K) | - |
| 023 | Sea level | SIOS SCD 4.1/4.2 (**S**); JERICO tide gauges (I); EMSO bottom pressure as proxy (K) | GLOSS, PSMSL/UHSLC [G2]; C3S [C2]; CMEMS SL TAC, In Situ TAC tide gauges [C4]; ESA CCI Sea Level | CMEMS (token; inferred) | - |
| 024 | Sea state | SIOS SCD 4.7 (**S**); JERICO wave buoys (I) | NCEI, BODC, AVISO [G2]; CMEMS Wave TAC [C4]; ESA CCI Sea State; EMODnet Physics waves | CMEMS, CDI (token; inferred) | - |
| 025 | Ocean surface stress | none found | CMEMS Wind TAC (K) [C4] | - | - |
| 026 | Ocean surface heat flux | SIOS SCD 4.6 "ocean heat budget" (**S**) | OceanSITES, ICOADS (K); ESA CCI OSHF [C5] | - | - |
| 027 | Sea ice | none in SIOS Core Data v1 [R-SIOS]; eLTER lake ice only | NSIDC, OSI SAF [G2]; C3S; CMEMS Sea Ice TAC; ESA CCI Sea Ice, SAGE; EMODnet Physics ice | - | - |
| 028 | Oxygen | Euro-Argo BGC O2, also on most EU Deep floats (V) [R-ARGO]; EMSO EGIM O2 (V); JERICO O2 (V); SeaDataNet CDI (I); DANUBIUS water quality (I) | CCHDO, BGC-Argo GDAC, OceanSITES, GLODAPv2 [G2]; CMEMS BGC (K); EMODnet Chemistry [R-EMOD] | Argo `argo_bgc` (open); WOD (open); EMOD-chem, CDI, CMEMS, WB2 (token) | - |
| 029 | Nutrients | Euro-Argo BGC nitrate (V); JERICO BGC (K); SeaDataNet (I); DANUBIUS (I); eLTER water chemistry (V, freshwater) | GLODAP, WOD (K); CMEMS BGC (K); EMODnet Chemistry DIN/PO4/SiO4 | Argo BGC (open); WOD (open); IHM `mon_*` chemistry (open, Dutch coast, not in registry); EMOD-chem, CDI, CMEMS, WB2 (token) | - |
| 030 | Ocean inorganic carbon | ICOS Ocean fCO2 from 11 VOS lines and 10 stations, to SOCAT (V) [R-ICOS-O]; Euro-Argo BGC pH (V); EMSO optional pH, pCO2 (V); JERICO carbonate theme (I) | GLODAPv2, SOCAT, CCHDO, NCEI OCADS [G2]; CMEMS acidification indicators [C4] | Argo BGC pH (open); CDI, EMOD-chem (token; inferred); no ICOS node | - |
| 031 | Transient tracers | SeaDataNet CDI (K) | GLODAP, CCHDO (K) | CDI (token; inferred) | - |
| 032 | Ocean nitrous oxide | none found (ICOS N2O is atmospheric) | MEMENTO (K) | CDI (token; inferred) | - |
| 033 | Ocean colour | Euro-Argo BGC chlorophyll, backscatter, irradiance (V); SIOS SCD 4.9 chlorophyll (**S**); JERICO chl-a (V) | OC-CCI, NASA OBPG (K); C3S; CMEMS OC TAC; ESA CCI Ocean Colour | Argo BGC (open); EMOD-chem, WB2 (token) | - |
| 034 | Plankton | EMBRC EMO BON water-column omics, reads in ENA (V) [R-EMBRC]; Euro-Argo chl/particles as proxy (V); JERICO phytoplankton (V); DANUBIUS biology (I) | CPR, IGMETS, OBIS [G2]; ESA CCI PHYTO-CCI; EMODnet Biology/EurOBIS | WOD plankton (open); IHM plankton (open, not in registry) | - |
| 035 | Marine habitat properties | EMBRC EMO BON sediment and ARMS hard-substrate (I) | GCRMN, AIMS, OBIS [G2]; EMODnet Biology/Seabed Habitats | IHM benthos/vegetation (open, not CF-named) | - (NVS gives no CF name) |

## Land (EXV036-EXV055)

| EXV | GCOS ECV | European RIs (variables; tag; source) | Global / Copernicus hosts | MARIS Beacon | Workflow |
| --- | --- | --- | --- | --- | --- |
| 036 | Groundwater | eLTER SOHYD_006/059/062/064, groundwater chemistry and isotopes but no level (V, partial) [R-eLTER]; EPOS GNSS loading (K, research-grade) | GCOS: IGRAC/GGMN, G3P [G2][R-IGRAC]; C3S TWS/groundwater [C2] | - | - |
| 037 | Lakes | eLTER SOHYD_004 profiles, _011 ice cover, _174 Secchi (V); DANUBIUS water quality, sediment, DOM (V) [R-DAN] | GCOS: HYDROLARE, ILEC, DAHITI, Hydroweb, Lakes-CCI [G2]; CLMS lake temperature/water quality/level/ice [R-CLMS]; C3S; ESA CCI Lakes | - | - (NVS gives no CF name) |
| 038 | River discharge | eLTER SOHYD_010 water level (V); DANUBIUS "hydrological" category (I); EMODnet Physics river runoff (V, non-RI) | GCOS: GRDC, WHOS [G2][R-GRDC]; ESA CCI River Discharge; Hydroweb river levels (K) | - | - |
| 039 | Soil moisture | SIOS SCD 3.1 (**S**); ICOS ecosystem SWC profiles (V, snippet) [R-ICOS-E]; eLTER SOHYD_168 (V) | GCOS: ISMN, CCI, C3S, SMAP, SMOS [G2]; CLMS SWI/SSM; ESA CCI Soil Moisture | - | - |
| 040 | Terrestrial water storage | none found (EPOS GNSS loading is research-grade, K) | GRACE, G3P (K); C3S [C2] | - | - (NVS gives no CF name) |
| 041 | Snow | SIOS SCD 2.8-2.11 depth, SWE, cover (**S**); eLTER SOHYD_012 (V); ICOS ecosystem snow height (V, snippet); INTERACT stations (I) [R-INT] | GCOS: NSIDC, Global Snow Lab [G2]; CLMS snow; C3S; ESA CCI Snow | - | - |
| 042 | Glaciers | SIOS SCD 2.1-2.3 mass balance, elevation, velocity (**S**); eLTER SOHYD_164-166 (V) | GCOS: WGMS/GTN-G, GLIMS, RGI, GlaThiDa [G2][R-WGMS]; C3S; ESA CCI Glaciers | - | - |
| 043 | Ice sheets and ice shelves | none found | NSIDC, IMBIE (K); C3S; ESA CCI Ice Sheets (Antarctic, Greenland) | - | - |
| 044 | Permafrost | SIOS SCD 2.4-2.7 (**S**); INTERACT stations (I) | GCOS: GTN-P (CALM, TSP) [G2][R-GTNP]; ESA CCI Permafrost | - | - |
| 045 | FAPAR | ICOS ecosystem PPFD in, out and below canopy (K) | CLMS FAPAR [R-CLMS]; C3S; ESA CCI Vegetation Parameters | - | - |
| 046 | Leaf area index | ICOS ecosystem LAI/GAI, processed at ETC (V, snippet) [R-ICOS-E]; eLTER SOBIO_025/026 (V) | CLMS LAI; C3S; ESA CCI Vegetation Parameters | - | - |
| 047 | Albedo | eLTER SOATM_028 radiation (I, partial); ICOS ecosystem SW in/out (K) | CLMS albedo (snippet); C3S [C2] | - | - |
| 048 | Land-surface temperature | ICOS ecosystem LW out (K) | CLMS LST; C3S (K); ESA CCI LST | - | - |
| 049 | Above-ground biomass | ICOS ecosystem AGB by allometry (V, snippet); eLTER SOBIO_023/024/177, vegetation LiDAR SOBIO_140 (V) | ESA CCI Biomass [C5]; CLMS DMP/NPP proxy | - | - |
| 050 | Land cover | eLTER SOBIO_015/017, vegetation composition and phenology (I, partial); LifeWatch VRE layers (I) [R-LW] | CLMS global and European land cover; C3S; ESA CCI Land Cover, HR Land Cover | - | - |
| 051 | Soil carbon | ICOS ecosystem soil C and N (V, slides) [R-ICOS-E]; eLTER SOGEO_001/003 (V) | GCOS: HWSD, GSOCmap [G2] | - | - |
| 052 | Fire | none found | C3S burnt area/FRP; CAMS GFAS; CLMS burnt area; ESA CCI Fire [G2][C2][C3][R-CLMS] | - | - |
| 053 | Anthropogenic GHG fluxes | ICOS Carbon Portal emission and inversion products (K); ICOS ecosystem fluxes are natural, not anthropogenic (V) | CAMS inversion-optimised fluxes [C3]; UNFCCC inventories, EDGAR (K) | - | - |
| 054 | Evaporation from land | ICOS ecosystem LE/H eddy covariance (V) [R-ICOS-E]; eLTER SOATM_176 LE, SOBIO_091 transpiration (V) | FLUXNET [R-FLUX]; GLEAM (K); CLMS ETA; ESA CCI Land Evaporation | - | - |
| 055 | Anthropogenic water use | none found | FAO AQUASTAT (K); ESA CCI Anthropogenic Water Use [C5] | - | - |

**RIs with no direct land-ECV link.** Three RIs have no direct link: AnaEE ERIC,
LifeWatch ERIC and EPOS. Their sources are [R-AnaEE], [R-LW] and [R-EPOS].

- **AnaEE** runs more than 60 manipulation facilities, but it publishes no
  observation variables and has no data portal.
- **LifeWatch** has a metadata catalogue (2,454 datasets, about 30 VREs,
  NaaVRE among them), but names no ECV or land-cover product.
- **EPOS** offers GNSS position, velocity and strain only. Its GNSS water
  vapour (GFZ "EPOS8" products) is an indirect link.

## Summary

### ECVs that no European RI covers

No European environmental RI page, and no RI document read, links an RI to
these ECVs:

- **Atmosphere:** EXV010 Earth radiation budget (top-of-atmosphere satellite:
  CERES, C3S); EXV012 Lightning (WWLLN; no Copernicus or CCI product either).
- **Ocean:**
  - EXV025 Ocean surface stress (CMEMS Wind TAC);
  - EXV027 Sea ice (C3S, CMEMS, OSI SAF, ESA CCI; not in SIOS Core Data v1);
  - EXV031 Transient tracers and EXV032 Ocean nitrous oxide (GLODAP, CCHDO,
    MEMENTO; SeaDataNet holds them at most, K).
- **Land:**
  - EXV040 Terrestrial water storage (GRACE, G3P, C3S);
  - EXV043 Ice sheets and ice shelves (IMBIE, C3S, ESA CCI);
  - EXV052 Fire (C3S, CAMS GFAS, CLMS, ESA CCI);
  - EXV053 Anthropogenic GHG fluxes (CAMS; ICOS products K only);
  - EXV055 Anthropogenic water use (AQUASTAT, ESA CCI).

These are satellite, model or inventory ECVs. They need a Copernicus, ESA CCI
or GCOS data-centre source, not an RI.

Several more are covered only partially or K, with ICOS ecosystem or eLTER at
most:

- EXV036 Groundwater (chemistry only, no level)
- EXV045 FAPAR
- EXV047 Albedo
- EXV048 Land-surface temperature
- EXV050 Land cover

### Which RIs would add the most ECVs to `conf_ri_registry`

The registry reads Beacon tables, so the cheapest additions are open Beacon
nodes. Other RIs need a new adapter, because no RI API speaks CF standard names
the way Beacon does. ECV gains are counted against the 11 ECVs found today.

| Rank | Source | New ECVs (EXV) | Cost | Caveat |
| --- | --- | --- | --- | --- |
| 1 | **Euro-Argo** on `beacon-argo` (open) | up to 9: 017, 018, 019, 020, 028, 029, 030 (pH), 033 (chl), 034 (proxy) | Flip `token_required` to `False` for the Argo entry and add `argo_bgc` | No data query since the 2026-11-25 planning error; check that first. Floats sit off-shelf, so the default North Sea/central Europe window (lon 0-20, lat 45-55) will return few or no profiles. Test with an ocean window. |
| 2 | **NOAA WOD** on `beacon-wod` (open; not an RI) | 017, 018, 019, 020, 028, 029, 034, mostly the same as Argo | One registry entry (`easy-wod`) | Rate-limited demo node |
| 3 | **ICOS** (Carbon Portal SPARQL/REST, no Beacon table) | up to 10: 006 (K), 030, 039, 046, 049, 051, 054 are new; it adds stations for 001-004 and 013 | New adapter | Many links are V or K. ICOS has no Beacon node today. |
| 4 | **SIOS** (METSIS/OPeNDAP) | about 12 new, all stated: 006, 021, 023, 024, 026, 033, 039, 041, 042, 044, plus Svalbard ocean T/S | New adapter | Svalbard only (lat ~74-81), so outside the default window |
| 5 | **eLTER** (DAR, DEIMS) | about 10, all V: 037, 038, 039, 041, 042, 046, 049, 051, 054, 036 (partial) | New adapter; data are heterogeneous, not CF-named | Best European land RI on paper. Hard to query generically. |
| 6 | IRISCC grids, ERA5 on Beacon (open; not RIs) | none new. They add gridded sources for 002, 005, 014, 015, 016; ERA5 turns 005 Precipitation from 0 rows into data | Registry entries, but they are gridded (x, y, year), not station rows | The workflow's height and site columns need a gridded variant |
| 7 | `beacon-ihm` (Rijkswaterstaat; open; not an RI) | 029, 034, 035 for the Dutch coast | Many tables, non-CF names | Regional only |

Two RIs are not worth adding as ECV sources: **ACTRIS cloud remote sensing**,
which is not on Beacon, and **EMSO, JERICO, EMBRC and DANUBIUS**. EMSO has an
ERDDAP (`erddap.emso.eu`) that could serve 018, 020, 022, 028 and 030, but they
overlap Argo. JERICO data go out through CMEMS and EMODnet. EMBRC data are omics
in ENA. DANUBIUS has no public portal.

### Where a MARIS token would unlock data

A Blue-Cloud2026 "Beacon Beta" token (request via info@maris.nl) opens the
401 nodes. Their tables were not visible, so the ECV lists below are inferred
from each node's described domain:

- **SeaDataNet CDI** (`beacon-cdi`, `-incremental`; `-ts` was 502).
  Multidisciplinary European in-situ data, so potentially every ocean ECV with
  a P02 code:
  - 017-024 and 028-030;
  - 031 Transient tracers and 032 Ocean N2O, which no open node serves.
  This is the only realistic RI route to 031 and 032.
- **CMEMS in-situ** (`beacon-cmems`), plus **CORA** profiles and time series
  (`beacon-cora-pr`, `-ts`). They would add the ocean ECVs that no open node
  serves:
  - 021 Surface currents
  - 022 Subsurface currents
  - 023 Sea level, from tide gauges
  - 024 Sea state, from wave buoys
  CMEMS in-situ also adds coastal T/S and BGC.
- **EMODnet Chemistry** (`beacon-emod-chem`) and **WorkBench 2**
  (`beacon-wb2-eutrophication`): 028, 029, 030 and 033 in European shelf seas.
  These fit the default window, which Argo does not.
- **WorkBench 1** (`beacon-wb1-ts`): merged T/S, covering 017-020.

A token unlocks no atmosphere or land ECV. On Beacon, land ECVs exist on no
node at all, and only the open IHM node touches marine habitats (035).

### Follow-ups (not done here)

1. `beacon-argo` answers without a token, but `conf_ri_registry` still has
   `token_required: True` for Argo, so the coverage run skips it. Re-test an
   Argo query, then flip the flag.
2. Add `argo_bgc` and `easy-wod` registry entries, and re-run
   `scripts/validate_all_ecvs.py` with an ocean window.
3. The default window lon 0-20, lat 45-55 is mostly land and shelf sea. Ocean
   ECVs need a per-domain default window.
4. For land ECVs, the realistic sources are Copernicus (CLMS, C3S) and ESA CCI
   gridded products, not RIs. That would be a new, gridded source type in the
   workflow.

## Sources

GCOS, GOOS and Copernicus:

- [G1] GCOS ECV list: https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables
- [G2] GCOS per-ECV pages: `.../essential-climate-variables/{slug}`, for precipitation, surface-temperature, surface-radiation-budget, upper-air-temperature, carbon-dioxide-methane-other-greenhouse-gases, ozone, aerosols, sea-surface-temperature, subsurface-temperature, sea-surface-salinity, surface-currents, sea-state, sea-level, sea-ice, oxygen, inorganic-carbon, plankton, marine-habitats, groundwater, lakes, river-discharge, soil-moisture, snow, glaciers, permafrost, fire, soil-carbon. GCOS calls its data-centre lists "not complete".
- [G3] GCOS-245, *The 2022 GCOS ECVs Requirements*: https://library.wmo.int/viewer/58111 (full text not read)
- [G4] ECV rationalisation, C3S General Assembly 2024 (search snippet): https://climate.copernicus.eu/sites/default/files/custom-uploads/7th%20GA%20C3S/Presentations/Day%202/S1/02-s18.06.2024_sFromObstoECVs_ECV_Rationalization_Thorrne_C3S.pdf
- [G5] GOOS EOVs: https://goosocean.org/what-we-do/framework/essential-ocean-variables/ . The EOV specification sheets, PDFs on oceanexpert.org, could not be read as text.
- [C1] C3S ECV programme ("30 of the 55 ECVs"): https://www.ecmwf.int/en/newsletter/187/news/monitoring-climate-change-space-ecv-programme
- [C2] C3S theme pages: https://climate.copernicus.eu/atmospheric-physics , /atmospheric-composition , /ocean , /land-biosphere , /land-hydrology-cryosphere (the last from search results only)
- [C3] CAMS data: https://atmosphere.copernicus.eu/data
- [C4] CMEMS producers: https://marine.copernicus.eu/about/producers ; In Situ TAC: https://marineinsitu.eu/access-data/
- [C5] ESA CCI projects (34 projects, about 29 ECVs): https://climate.esa.int/en/projects/
- NVS EXV collection: http://vocab.nerc.ac.uk/collection/EXV/current/ (69 concepts, fetched 2026-11-26)

Research infrastructures:

- [R-ACTRIS] https://actris.eu/topical-centre/data-centre ; https://www.actris.eu/about/what-we-do/key-scientific-themes ; portal https://data.actris.eu/ . The Copernicus use case https://insitu.copernicus.eu/resources/use-cases-folder/actris-monitoring-of-the-state-of-the-atmosphere was seen only as a snippet.
- [R-IAGOS] https://www.iagos.org/iagos-core-instruments/ ; portal https://iagos.aeris-data.fr/ ; CORDIS IGAS https://cordis.europa.eu/project/id/312311/reporting (snippet); Petzold et al., Tellus B 2015 (snippet)
- [R-ICOS-A] ICOS Atmosphere Station Labelling Step 2: https://www.icos-cp.eu/sites/default/files/cmis/ICOS%20Atmospheric%20Station%20Labelling%20STEP%202.pdf ; https://www.icos-cp.eu/observations/atmosphere/stations ; portal https://data.icos-cp.eu/ ; UNFCCC poster https://unfccc.int/sites/default/files/resource/4.47%20ICOS_SBSTAposter_v2.pdf (snippet)
- [R-ICOS-E] https://www.icos-cp.eu/observations/ecosystem ; Ecosystem labelling Step 2 PDF and ancillary-vegetation instructions (snippets)
- [R-ICOS-O] https://www.icos-otc.org/measurements ; https://www.icos-otc.org/data-levels-quality-access ; https://erddap.icos-cp.eu/
- [R-SIOS] SIOS Core Data, Appendix 1 (v1, April 2020): https://sios-svalbard.org/sites/sios-svalbard.org/files/common/CoreData_Appendix_v1.pdf ; https://sios-svalbard.org/CoreData ; SESS 2021 chapter 6: https://zenodo.org/records/5751970 ; portal https://sios-svalbard.org/metsis/search
- [R-EPOS] https://www.epos-eu.org/tcs ; https://www.epos-eu.org/tcs/gnss-data-and-products ; GFZ ZTD/IWV: https://b2find.eudat.eu/dataset/6f4c75ed-92ad-5208-ae30-eec5b500a302
- [R-ARGO] https://euro-argo.eu/Outreach/Outreach-material/OneArgo ; https://www.euro-argo.eu/Argo-Data-access ; https://dataselection.euro-argo.eu/ ; https://fleetmonitoring.euro-argo.eu/
- [R-EMSO] https://emso.eu/ ; ERDDAP https://erddap.emso.eu/erddap/ ; EGIM paper https://www.frontiersin.org/articles/10.3389/fmars.2022.801033/full
- [R-SDN] https://www.seadatanet.org/ ; https://cdi.seadatanet.org/search
- [R-JERICO] https://www.jerico-ri.eu/ ; https://www.jerico-ri.eu/data-access/ ; https://www.blue-cloud.org/data-infrastructures/jerico-ri
- [R-EMBRC] EMO BON data release, Biodiversity Data Journal 13 (2025): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11923592/ ; https://www.embrc.eu/
- [R-DAN] https://danubius-ri.eu/architecture/data-center/ ; https://danubius-ri.eu/architecture/supersites/ ; https://gis.geoecomar.ro/danubius/
- [R-eLTER] eLTER Standard Observations: https://elter-ri.eu/standard-observations-spheres/atmosphere (also /hydrosphere, /geosphere, /biosphere) ; https://dar.elter-ri.eu/
- [R-AnaEE] https://www.anaee.eu/
- [R-LW] https://metadatacatalogue.lifewatch.eu ; https://search.lifewatch.eu
- [R-INT] INTERACT station catalogue: https://eu-interact.org/publication/interact-station-catalogue-2020/

Other data hosts:

- [R-EMOD] https://emodnet.ec.europa.eu/en/physical-parameters , /en/chemistry , /en/biology
- [R-GTNP] https://gtnp.arcticportal.org/
- [R-WGMS] https://wgms.ch/data_databaseversions/
- [R-GRDC] https://grdc.bafg.de/ ; https://portal.grdc.bafg.de/
- [R-IGRAC] https://un-igrac.org/data/dataset/
- [R-CLMS] https://documentation.dataspace.copernicus.eu/Data/CopernicusServices/CLMS.html (land.copernicus.eu refused the connection)
- [R-FLUX] https://fluxnet.org/

Beacon and workflow:

- Beacon nodes: [REPORT-MARIS-BEACON-NODES-2026-11-26.md](REPORT-MARIS-BEACON-NODES-2026-11-26.md)
- Workflow coverage: [results/coverage/ECVs-coverage.md](results/coverage/ECVs-coverage.md)
- Registry: `scripts/make_notebook.py`, `conf_ri_registry`

Pages that failed or were read only as snippets:

| Page | What happened |
| --- | --- |
| land.copernicus.eu, insitu.copernicus.eu ACTRIS page | refused the connection |
| GCOS-245 full text, GOOS EOV spec sheets, ICOS handbook PDFs, UNFCCC poster | did not render as text |
| euro-argo.eu and seadatanet.org | returned 503 in the earlier ENVRI survey, but this survey read the pages cited above |
