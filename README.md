# ECV (EXV)

| Abbreviation | Description                                                          |
| ------------ | -------------------------------------------------------------------- |
| ENVRI-HUB    | Data Portal of the European Environmental Research Infrastructures   |
|   NERC       | Natural Environment Research Council, UK                             |
|   AnaEE      | Analysis and Experimentation on Ecosystems                           |
|   ERA5       | ECMWF Reanalysis v5 (ERA5)                                           |
|   ARGO       | Real-time global ocean in situ observing system                      |
|   IRISCC     | Integrated Research Infrastructure Services for Climate Change Risks |
|   ICOS       | Integrated Carbon Observation System                                 |
|   CDI        | SeaDataNet Common Data Index (CDI) service                           |
|   ACTRIS     | Aerosol, Clouds, and Trace Gases Research Infrastructure             |
|   IAGOS      | In-service Aircraft for a Global Observing System                    |

## ENVRI-HUB

### envrihub

[ENVRI-Hub Python library](https://gitlab.a.incd.pt/envri-hub-next/vre-lib), streamline interaction with the ENVRI-Hub APIs, providing a pythonic facade to data and service access

### Methods

* search_catalogue
* fetch_from_catalogue

### Supports

#### AnaEE

Analysis and Experimentation on Ecosystems

##### getNearestStationData

* seriesID
* averageTemp
* precipitation
* elevation

##### getStationData

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

* seriesID
* maxTemp
* minTemp
* precipitation
* idCode

#### ARGO

Real-time global ocean in situ observing system

##### Source

* erddap: the Ifremer erddap server (Default)
* gdac: an Argo GDAC server or any other GDAC-compliant local folder
* argovis: the Argovis server

##### Dataset

* phy: physical parameters
* bgc: biogeochemical parameters

