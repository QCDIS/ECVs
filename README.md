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

