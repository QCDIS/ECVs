# ECV (EXV)

| Abbreviation  | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| **ENVRI-HUB** | Data Portal of the European Environmental Research Infrastructures   |
| AnaEE         | Analysis and Experimentation on Ecosystems                           |
| ERA5          | ECMWF Reanalysis v5 (ERA5)                                           |
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

### envrihub

[ENVRI-Hub Python library](https://gitlab.a.incd.pt/envri-hub-next/vre-lib), streamline interaction with the ENVRI-Hub APIs, providing a pythonic facade to data and service access

### Methods

* `search_catalogue`: Performs search on the ENVRI-Hub's catalogue
* `fetch_from_catalogue`: Retrieves a specific resource from the ENVRI-Hub's catalogue

### Supports

#### AnaEE

Analysis and Experimentation on Ecosystems, [API](https://developer.anaee.eu/apis)

##### getNearestStationData

Output:
* seriesID
* averageTemp
* precipitation
* elevation

##### getStationData

Output:
* seriesID
* averageTemp
* maxTemp
* minTemp
* windSpeed
* maxWindSpeed
* windGust
* precipitation
* stationPressure
* RH
* RHMin
* RHMax
* RAD
* leafWetness
* elevation

##### getRasterData

Output:
* seriesID
* maxTemp
* minTemp
* precipitation
* idCode

#### ARGO

Real-time global ocean in situ observing system, [Data access](https://www.euro-argo.eu/Argo-Data-access)

##### Source

* `erddap`: the Ifremer erddap server (Default)
* `gdac`: an Argo GDAC server or any other GDAC-compliant local folder
* `argovis`: the Argovis server

##### Dataset

* `phy`: physical parameters
* `bgc`: biogeochemical parameters

