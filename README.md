# ECV (EXV)

## About Essential Climate Variables

An Essential Climate Variable (ECV) is a physical, chemical or biological variable or a group of linked variables that critically contributes to the characterization of Earth’s climate. Global Climate Observing System ([GCOS](https://gcos.wmo.int/site/global-climate-observing-system-gcos)) currently specifies [55 ECVs](https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables).

ECV datasets provide the empirical evidence needed to understand and predict the evolution of climate, to guide mitigation and adaptation measures, to assess risks and enable attribution of climate events to underlying causes, and to underpin climate services. They are required to support the work of the UNFCCC and the IPCC.

### ECV are identified based on the following criteria:

* Relevance: The variable is critical for characterizing the climate system and its changes.
* Feasibility: Observing or deriving the variable on a global scale is technically feasible using proven, scientifically understood methods.
* Cost effectiveness: Generating and archiving data on the variable is affordable, mainly relying on coordinated observing systems using proven technology, taking advantage where possible of historical datasets.

### ECV Observation Requirements

Current ECV requirements according to the 2022 GCOS ECV Requirements ([GCOS-245](https://library.wmo.int/records/item/58111-the-2022-gcos-ecvs-requirements)):

* Atmosphere
* Ocean
* Land

![img_ECVs-List.png](documentation/images/ECVs-List.png "ECVs List")

## ENVRI-HUB

Data Portal of the European Environmental Research Infrastructures

[ENVRI-Hub Python library](https://gitlab.a.incd.pt/envri-hub-next/vre-lib), streamline interaction with the ENVRI-Hub APIs, providing a pythonic facade to data and service access

* `search_catalogue`: Performs search on the ENVRI-Hub's catalogue
* `fetch_from_catalogue`: Retrieves a specific resource from the ENVRI-Hub's catalogue

| Abbreviation    | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| **Data Portal** | https://envrihub.vm.fedcloud.eu/                                     |
| AnaEE           | Analysis and Experimentation on Ecosystems                           |
|   ERA5          | ECMWF Reanalysis v5 (ERA5), ECMWF                                    |
| ARGO            | Real-time global ocean in situ observing system                      |
| IRISCC          | Integrated Research Infrastructure Services for Climate Change Risks |
| ICOS            | Integrated Carbon Observation System                                 |
| CDI             | SeaDataNet Common Data Index (CDI) service                           |
| ACTRIS          | Aerosol, Clouds, and Trace Gases Research Infrastructure             |
| IAGOS           | In-service Aircraft for a Global Observing System                    |
| EPOS            | European Plate Observing System                                      |
| **NERC**        | Natural Environment Research Council, UK                             |
| I-ADOPT         | InteroperAble Descriptions of Observable Property                    |
| NVS             | The NERC Vocabulary Server                                           |
| SPARQL          | The NERC SPARQL queries for the NVS vocab server                     |

### Data Portal

* [Search](https://search.envri.eu/search/genericpages/genericpages?page=home)
* [Catalogue Of Services (COS)](https://catalogue.staging.envri.eu/)

#### AnaEE

Analysis and Experimentation on Ecosystems, [API](https://developer.anaee.eu/apis)

##### getNearestStationData

Example output:

| date | seriesID | averageTemp | precipitation | idGroup | idCode | stationName | country | elevation | geography |
| ---- | -------- | ----------- | ------------- | ------- | ------ | ----------- | ------- | --------- | --------- |
| 2022-06-14 00:00:00+02:00 | 11 | 13.5 | 0.0 | regione-liguria | CABAN | Cabanne | IT | 809.0 | POINT (9.3408 44.4883) |


##### getStationData

Example output:

| date | seriesID | averageTemp | maxTemp | minTemp | windSpeed | maxWindSpeed | windGust | precipitation | stationPressure | RHMin | RHMax | RAD | leafWetness | idGroup | idCode | stationName | country | elevation |
| ---- | -------- | ----------- | ------- | ------- | --------- | ------------ | -------- | ------------- | --------------- | ----- | ----- | --- | ----------- | ------- | ------ | ----------- | ------- | --------- |
| 2022-06-14 00:00:00+02:00 | 11 | NaN | NaN | NaN | NaN | NaN | 0.0 | NaN | NaN | NaN | NaN | NaN | regione-liguria | AGORR | Alpe Gorreto | IT | 915.0 |
    

##### getRasterData

Example output:

| date | seriesID | averageTemp | maxTemp | minTemp | windSpeed | maxWindSpeed | windGust | precipitation | stationPressure | RHMin | RHMax | RAD | leafWetness | idGroup | idCode | stationName | country | elevation |
| ---- | -------- | ----------- | ------- | ------- | --------- | ------------ | -------- | ------------- | --------------- | ----- | ----- | --- | ----------- | ------- | ------ | ----------- | ------- | --------- |
| 2022-06-14 00:00:00+02:00 | 11 | NaN | NaN | NaN | NaN | NaN | 0.0 | NaN | NaN | NaN | NaN | NaN | regione-liguria | AGORR | Alpe Gorreto | IT | 915.0 |


##### GetEraData

Example output:

| station_id | idGroup | Country | firstRecord | lastRecord | Elevation | Latitude | Longitude | nuts1 | nuts2 | nuts3 | geometry | Date | date_index | d2m | t2m | u10 | v10 | ssrd | tp | rh | windspeed |
| ---------- | ------- | ------- | ----------- | ---------- | --------- | -------- | --------- | ----- | ----- | ----- | -------- | ---- | ---------- | --- | --- | --- | --- | ---- | -- | -- | --------- | 
| 9.50-44.25 | Era5 | Italia | 1900-01-01 00:00:00+00:00 | 2024-09-18 23:00:00+00:00 | 268.46797089999995 | 44.25 | 9.5 | Nord-Ovest | Liguria | Genova | POINT(9.5 44.25) | 2022-06-15 00:00:00+00:00 | 2022-06-15 00:00:00+00:00 | 19.75967612471516 | 24.44530128934332 | -1.9472449479938327 | -2.374912076563004 | -2.3283064365386963e-10 | 0.0 | 0.751407767589943 | 3.071151292087758 |


#### ARGO

Real-time global ocean in situ observing system, [Data access](https://www.euro-argo.eu/Argo-Data-access)

##### Source

* `erddap`: the Ifremer erddap server (Default)
* `gdac`: an Argo GDAC server or any other GDAC-compliant local folder
* `argovis`: the Argovis server

##### Dataset

* `phy`: physical parameters
* `bgc`: biogeochemical parameters

## NERC

### [ESV list](http://vocab.nerc.ac.uk/collection/EXV/current/)

| ID | Preferred Label |
| -- | --------------- |
| [EXV049](https://gcos.wmo.int/en/essential-climate-variables/biomass) | Above-ground biomass |
| [EXV016](https://gcos.wmo.int/en/essential-climate-variables/aerosols) | Aerosol properties |
| [EXV047](https://gcos.wmo.int/en/essential-climate-variables/albedo) | Albedo |
| [EXV053](https://gcos.wmo.int/en/essential-climate-variables/ghg-fluxes) | Anthropogenic greenhouse gas fluxes |
| [EXV055](https://gcos.wmo.int/en/essential-climate-variables/water-use) | Anthropogenic water use |
| [EXV068](https://goosocean.org/document/36269) | Benthic invertebrate abundance and distribution |
| [EXV013](https://gcos.wmo.int/en/essential-climate-variables/ghg) | Carbon dioxide, methane and other greenhouse gases |
| [EXV011](https://gcos.wmo.int/en/essential-climate-variables/clouds) | Cloud properties |
| [EXV063](https://goosocean.org/document/17512) | Coral cover and composition |
| [EXV010](https://gcos.wmo.int/en/essential-climate-variables/earth-radiation) | Earth radiation budget |
| [EXV054](https://gcos.wmo.int/en/essential-climate-variables/evaporation) | Evaporation from land |
| [EXV052](https://gcos.wmo.int/en/essential-climate-variables/fire) | Fire |
| [EXV059](https://goosocean.org/document/17510) | Fish abundance and distribution |
| [EXV045](https://gcos.wmo.int/en/essential-climate-variables/fapar) | Fraction of absorbed PAR |
| [EXV042](https://gcos.wmo.int/en/essential-climate-variables/glaciers) | Glaciers |
| [EXV036](https://gcos.wmo.int/en/essential-climate-variables/groundwater) | Groundwater |
| [EXV043](https://gcos.wmo.int/en/essential-climate-variables/ice-sheets-ice-shelves) | Ice sheets ad ice shelves |
| [EXV037](https://gcos.wmo.int/en/essential-climate-variables/lakes) | Lakes |
| [EXV050](https://gcos.wmo.int/en/essential-climate-variables/land-cover) | Land cover |
| [EXV048](https://gcos.wmo.int/en/essential-climate-variables/land-temperature) | Land-surface temperature |
| [EXV046](https://gcos.wmo.int/en/essential-climate-variables/lai) | Leaf area index |
| [EXV012](https://gcos.wmo.int/en/essential-climate-variables/lightning) | Lightning |
| [EXV065](https://goosocean.org/document/17515) | Macroalgal canopy cover and composition |
| [EXV066](https://goosocean.org/document/17514) | Mangrove cover and composition |
| [EXV035](https://gcos.wmo.int/en/essential-climate-variables/marine-habitats/) | Marine habitat properties |
| [EXV062](https://goosocean.org/document/36266) | Marine mammal abundance and distribution |
| [EXV067](https://goosocean.org/document/36264) | Microbe biomass and diversity |
| [EXV029](https://goosocean.org/document/17474) | Nutrients |
| [EXV058](https://goosocean.org/document/32488) | Ocean bottom pressure |
| [EXV033](https://goosocean.org/document/19959) | Ocean colour |
| [EXV030](https://goosocean.org/document/17475) | Ocean inorganic carbon |
| [EXV032](https://goosocean.org/document/17478) | Ocean nitrous oxide |
| [EXV069](https://goosocean.org/document/22567) | Ocean sound |
| [EXV026](https://goosocean.org/document/17472) | Ocean surface heat flux |
| [EXV025](https://goosocean.org/document/17463) | Ocean surface stress |
| [EXV028](https://goosocean.org/document/17473) | Oxygen |
| [EXV014](https://gcos.wmo.int/en/essential-climate-variables/ozone) | Ozone |
| [EXV044](https://gcos.wmo.int/en/essential-climate-variables/permafrost) | Permafrost |
| [EXV056](https://goosocean.org/document/17507) | Phytoplankton biomass and diversity |
| [EXV034](https://gcos.wmo.int/en/essential-climate-variables/plankton/) | Plankton |
| [EXV005](https://gcos.wmo.int/en/essential-climate-variables/precipitation) | Precipitation |
| [EXV015](https://gcos.wmo.int/en/essential-climate-variables/precursors) | Precursors (supporting the aerosol and ozone ECVs) |
| [EXV038](https://gcos.wmo.int/en/essential-climate-variables/rivers) | River discharge |
| [EXV027](https://goosocean.org/document/17464) | Sea ice |
| [EXV023](https://goosocean.org/document/17465) | Sea level |
| [EXV024](https://goosocean.org/document/17462) | Sea state |
| [EXV060](https://goosocean.org/document/36268) | Sea turtles abundance and distribution |
| [EXV019](https://goosocean.org/document/17470) | Sea-surface salinity |
| [EXV017](https://goosocean.org/document/17466) | Sea-surface temperature |
| [EXV061](https://goosocean.org/document/36267) | Seabirds abundance and distribution |
| [EXV064](https://goosocean.org/document/17513) | Seagrass cover and composition |
| [EXV041](https://gcos.wmo.int/en/essential-climate-variables/snow) | Snow |
| [EXV051](https://gcos.wmo.int/en/essential-climate-variables/soil-carbon) | Soil carbon |
| [EXV039](https://gcos.wmo.int/en/essential-climate-variables/soil-moisture) | Soil moisture |
| [EXV022](https://goosocean.org/document/17469) | Subsurface currents |
| [EXV020](https://goosocean.org/document/17471) | Subsurface salinity |
| [EXV018](https://goosocean.org/document/17467) | Subsurface temperature |
| [EXV021](https://goosocean.org/document/17468) | Surface currents |
| [EXV001](https://gcos.wmo.int/en/essential-climate-variables/pressure) | Surface pressure |
| [EXV006](https://gcos.wmo.int/en/essential-climate-variables/surface-radiation) | Surface Radiation Budget |
| [EXV002](https://gcos.wmo.int/en/essential-climate-variables/surface-temperature) | Surface temperature |
| [EXV004](https://gcos.wmo.int/en/essential-climate-variables/surface-vapour) | Surface water vapour |
| [EXV003](https://gcos.wmo.int/en/essential-climate-variables/surface-wind) | Surface wind speed and direction |
| [EXV040](https://gcos.wmo.int/en/essential-climate-variables/tws/) | Terrestrial water storage |
| [EXV031](https://goosocean.org/document/17476) | Transient tracers |
| [EXV007](https://gcos.wmo.int/en/essential-climate-variables/upper-temperature) | Upper-air Temperature |
| [EXV009](https://gcos.wmo.int/en/essential-climate-variables/upper-vapour) | Upper-air water vapour |
| [EXV008](https://gcos.wmo.int/en/essential-climate-variables/upper-wind) | Upper-air wind speed and direction |
| [EXV057](https://goosocean.org/document/17509) | Zooplankton biomass and diversity |

### [I-ADPOT](https://i-adopt.github.io/)

* [Framework](https://github.com/i-adopt/framework/)
* [Framework ontology](https://i-adopt.github.io/ontology/)
* [User Stories](https://github.com/i-adopt/users_stories/)
* [Visualizer](https://sirkos.github.io/iadopt-vis/)
* [Examples](https://github.com/mabablue/I-ADOPT-examples-playground/)
* []()
