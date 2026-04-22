# ECV (EXV)

| Abbreviation  | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| **ENVRI-HUB** | Data Portal of the European Environmental Research Infrastructures   |
| AnaEE         | Analysis and Experimentation on Ecosystems                           |
| ERA5          | ECMWF Reanalysis v5 (ERA5), ECMWF                                    |
| ARGO          | Real-time global ocean in situ observing system                      |
| IRISCC        | Integrated Research Infrastructure Services for Climate Change Risks |
| ICOS          | Integrated Carbon Observation System                                 |
| CDI           | SeaDataNet Common Data Index (CDI) service                           |
| ACTRIS        | Aerosol, Clouds, and Trace Gases Research Infrastructure             |
| IAGOS         | In-service Aircraft for a Global Observing System                    |
| EPOS          | European Plate Observing System                                      |
| **NERC**      | Natural Environment Research Council, UK                             |
| I-ADOPT       | InteroperAble Descriptions of Observable Property                    |
| NVS           | The NERC Vocabulary Server                                           |
| SPARQL        | The NERC SPARQL queries for the NVS vocab server                     |


## ENVRI-HUB

### Services

* [Search](https://search.envri.eu/search/genericpages/genericpages?page=home)
* [Catalogue Of Services (COS)](https://catalogue.staging.envri.eu/)

### Library

[ENVRI-Hub Python library](https://gitlab.a.incd.pt/envri-hub-next/vre-lib), streamline interaction with the ENVRI-Hub APIs, providing a pythonic facade to data and service access

* `search_catalogue`: Performs search on the ENVRI-Hub's catalogue
* `fetch_from_catalogue`: Retrieves a specific resource from the ENVRI-Hub's catalogue

### Supports

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

ESV list

| ID | Preferred Label |
| -- | --------------- |
| [EXV016](https://gcos.wmo.int/en/essential-climate-variables/aerosols) | Aerosol properties |
| [EXV047](https://gcos.wmo.int/en/essential-climate-variables/albedo) | Albedo |
| [EXV049](https://gcos.wmo.int/en/essential-climate-variables/biomass) | Above-ground biomass |
| [EXV011](https://gcos.wmo.int/en/essential-climate-variables/clouds) | Cloud properties |
| [EXV010](https://gcos.wmo.int/en/essential-climate-variables/earth-radiation) | Earth radiation budget |
| [EXV054](https://gcos.wmo.int/en/essential-climate-variables/evaporation) | Evaporation from land |
| [EXV045](https://gcos.wmo.int/en/essential-climate-variables/fapar) | Fraction of absorbed PAR |
| [EXV052](https://gcos.wmo.int/en/essential-climate-variables/fire) | Fire |
| [EXV013](https://gcos.wmo.int/en/essential-climate-variables/ghg) | Carbon dioxide, methane and other greenhouse gases |
| [EXV053](https://gcos.wmo.int/en/essential-climate-variables/ghg-fluxes) | Anthropogenic greenhouse gas fluxes |
| [EXV042](https://gcos.wmo.int/en/essential-climate-variables/glaciers) | Glaciers |
| [EXV036](https://gcos.wmo.int/en/essential-climate-variables/groundwater) | Groundwater |
| [EXV043](https://gcos.wmo.int/en/essential-climate-variables/ice-sheets-ice-shelves) | Ice sheets ad ice shelves |
| [EXV046](https://gcos.wmo.int/en/essential-climate-variables/lai) | Leaf area index |
| [EXV037](https://gcos.wmo.int/en/essential-climate-variables/lakes) | Lakes |
| [EXV050](https://gcos.wmo.int/en/essential-climate-variables/land-cover) | Land cover |
| [EXV048](https://gcos.wmo.int/en/essential-climate-variables/land-temperature) | Land-surface temperature |
| [EXV012](https://gcos.wmo.int/en/essential-climate-variables/lightning) | Lightning |
| [EXV035](https://gcos.wmo.int/en/essential-climate-variables/marine-habitats/) | Marine habitat properties |
| [EXV014](https://gcos.wmo.int/en/essential-climate-variables/ozone) | Ozone |
| [EXV044](https://gcos.wmo.int/en/essential-climate-variables/permafrost) | Permafrost |
| [EXV034](https://gcos.wmo.int/en/essential-climate-variables/plankton/) | Plankton |
| [EXV005](https://gcos.wmo.int/en/essential-climate-variables/precipitation) | Precipitation |
| [EXV015](https://gcos.wmo.int/en/essential-climate-variables/precursors) | Precursors (supporting the aerosol and ozone ECVs) |
| [EXV001](https://gcos.wmo.int/en/essential-climate-variables/pressure) | Surface pressure |
| [EXV038](https://gcos.wmo.int/en/essential-climate-variables/rivers) | River discharge |
| [EXV041](https://gcos.wmo.int/en/essential-climate-variables/snow) | Snow |
| [EXV051](https://gcos.wmo.int/en/essential-climate-variables/soil-carbon) | Soil carbon |
| [EXV039](https://gcos.wmo.int/en/essential-climate-variables/soil-moisture) | Soil moisture |
| [EXV006](https://gcos.wmo.int/en/essential-climate-variables/surface-radiation) | Surface Radiation Budget |
| [EXV002](https://gcos.wmo.int/en/essential-climate-variables/surface-temperature) | Surface temperature |
| [EXV004](https://gcos.wmo.int/en/essential-climate-variables/surface-vapour) | Surface water vapour |
| [EXV003](https://gcos.wmo.int/en/essential-climate-variables/surface-wind) | Surface wind speed and direction |
| [EXV040](https://gcos.wmo.int/en/essential-climate-variables/tws/) | Terrestrial water storage |
| [EXV007](https://gcos.wmo.int/en/essential-climate-variables/upper-temperature) | Upper-air Temperature |
| [EXV009](https://gcos.wmo.int/en/essential-climate-variables/upper-vapour) | Upper-air water vapour |
| [EXV008](https://gcos.wmo.int/en/essential-climate-variables/upper-wind) | Upper-air wind speed and direction |
| [EXV055](https://gcos.wmo.int/en/essential-climate-variables/water-use) | Anthropogenic water use |

