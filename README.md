# ECV (EXV)

| Abbreviation | Organization                                                         |
| ------------ | -------------------------------------------------------------------- |
| ENVRI-HUB    | Data Portal of the European Environmental Research Infrastructures   |
| AnaEE        | Analysis and Experimentation on Ecosystems                           |
| ERA5         | ECMWF Reanalysis v5 (ERA5)                                           |
| ARGO         | Real-time global ocean in situ observing system                      |
| IRISCC       | Integrated Research Infrastructure Services for Climate Change Risks |
| ICOS         | Integrated Carbon Observation System                                 |
| CDI          | SeaDataNet Common Data Index (CDI) service                           |
| ACTRIS       | Aerosol, Clouds, and Trace Gases Research Infrastructure             |
| IAGOS        | In-service Aircraft for a Global Observing System                    |
| NERC         | Natural Environment Research Council, UK                             |


# AnaEE Weather Data Access API

In this notebook we show how to invoke a simple weather data access service hosted by [AnaEE](https://anaee.eu).

## Setting up the environment

+ Install dependencies
+ Create Environmental Variables

These operations must be done *once*: after you install dependencies and declare environment variables, they will be there forever and you will only have to import them to allow your code to use them.

### Installing dependencies

In what follows, the exclamation mark `!` is used to send command directly to the Operating System. The following command installs the required dependencies detailed in the `requirements.txt` file present in the project root folder. Put the cursor in the following cell and press the `Run` button:

## The Weather Data API
The weather data API has four *methods*, you can see their details [here](https://developer.anaee.eu/api-details#api=crea-aa-italian-historical-wheater-series), they are:
+ `getNearestRasterData`: it gets the nearest raster point data to a given geometry;
+ `getNearestStationData`: it gets the station data within a certain geometry;
+ `getRasterData`: it gets the raster point data within a certain geometry;
+ `getStationData`: it gets the station data within a certain geometry;

The *interface* for all four methods includes the following parameters:
+ `startTime`: the start date of the weather data series, by default it's a month ago;
+ `endTime`: the end of the weather data series, by default it's right now;
+ `timeStep`: if we'd like daily or hourly data, by defautl it's "daily";
+ `wkt`: the area of interest expressed in [WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System) coordinates, as a [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) polygon. Mind that when specifying a polygon, vertices must be specified in counter-clockwise order;
+ `mode`: the desired output format, it can be either "csv", "json", or "bioma"; by default it's "csv".


# Argo Data Access

In this notebook we show how to invoke a simple argo data access service hosted by [Euro-Argo ERIC](https://euro-argo.eu).
This has been complemented in April 2025 with the interfacing to the Nerc Vocabulary Server for a seamless interrogation from the [EXV](https://vocab.nerc.ac.uk/collection/EXV/current/) vocabulary, through a sparql query (see section V).
2025/05/13 edit: Further fine-tuning are required to make sure all parameters are correctly matched-up, and Argopy well linked.

## I - Setting up the environment

Argo access services do not use any credentials or authentification. Thus, nothing more is necessary.

## II - Installing dependencies

To use this data access service, you need to install [ArgoPy python library](https://github.com/euroargodev/argopy?tab=readme-ov-file):

In what follows, the exclamation mark `!` is used to send command directly to the Operating System. The following command installs the required dependencies detailed in the `requirements.txt` file present in the project root folder. Put the cursor in the following cell and press the `Run` button: (To DO: ask Guillaume for the file for argopy

## III - Argopy library Usage

Argopy python library is a wrap-up library on top of several Argo data access services. The Argopy complete documentation is available online at the following link:
[here](https://argopy.readthedocs.io/en/latest/).\
There is also a nice "cheat sheet" summing up the main features and usage [here](https://argopy.readthedocs.io/en/latest/cheatsheet.html) \
The complete citation of this service is: \
`Maze, G., & Balem, K. (2020). argopy: A Python library for Argo ocean data analysis. Journal of Open Source Software, 5(53). //doi.org/10.21105/joss.02425`

The main basic functions that will be used in this example notebook are briefly described herebelow.

### III.1 - data source service selection
By default the service used to fetch Argo data is the [Ifremer erdapp server](http://www.ifremer.fr/erddap) : 
+ `argopy.set_options(src='erddap')` \
Other sources, including local copy or referenced copies of Argo datasets, can be fetched. Details are available [here](https://argopy.readthedocs.io/en/latest/user-guide/fetching-argo-data/data_sources.html)

### III.2 - argo dataset type depending on the ExV
Argo dataset inner architecture is differentiated whether they relate to a physical parameter (which are temperature and salinity) or a biogeochemical parameter (oxygen, nitrate, pH, light - irradiance -, particles - backscattering-, chlorophyll-A). How to handle this concretely will be presented hereafter.
+ `argopy.set_options(ds='bgc')`
+ `argopy.set_options(ds='phy')`

### III.3 - argo parameter selection
Argopy allows to select parameters to load within the dataFetcher method. By default, all available parameters are loaded. Details are available [here](https://argopy.readthedocs.io/en/latest/user-guide/fetching-argo-data/data_set.html#the-params-argument)
+ `argopy.DataFetcher(params='all')`
+ `argopy.DataFetcher(params='PSAL')`
+ `argopy.DataFetcher(params=['DOXY','PSAL'])`

Argopy also allows to query the Argo NVS tables. The [Argo parameter table](https://vocab.nerc.ac.uk/search_nvs/R03/) is of particular interest as it will be mapped with the [ExV](https://vocab.nerc.ac.uk/search_nvs/EXV/) table.
+ `from argopy import ArgoNVSReferenceTables`
+ `ArgoNVSReferenceTables().tbl('R03')`

### III.4 - spatio-temporal selection
The Argopy library allows to select data by using its DataFetcher method, which can be called in several manners :
 + defining a region: `ArgoSet = DataFetcher().region([-85 ,-45 ,10. ,20. ,0 ,10,'2023-01', '2025-06' ])`
 + selecting by Argo floats ID : `ArgoSet = DataFetcher().float([6902746, 6902747, 6902757])`
 + selecting specific profiles of an Argo float: `ArgoSet = DataFetcher().profile(6902746,34)`

The *interface* of the three methods are as follows:
+ *region* parameter consists in a list defining the area of interest as a rectangular space-time domain. The boundaries must be ordered as follows in the list:
   + western boundary in degreesEast within the `[-180 180]` domain;
   + eastern boundary in degreesEast within the `[-180 180]` domain;
   + southern boundary in degreesNorth within the `[-90 90]` domain;
   + northern boundary in degreesNorth within the `[-90 90]` domain;
   + upper layer in dbar within the `[0 6000]` domain : 0 means at the sea surface, 6000 means at the greatest depth possibly reached by an Argo float;
   + lower layer in dbar within the `[0 6000]` domain;
   + start time `[optionnal]` : the oldest date time in ISO-8601 format "YYYY-MM" or "YYYY-MM-DD" ;
   + end time `[optionnal]`: the most recent date time in ISO-8601 format. When not indicated, the whole dataset time domain is requested ;


+ *float* parameter is a list of floats wmo IDs `[integer]` (for more experience users)
+ *profile* parameters consists in a float wmo ID and either a single profile as in the above example or an array containing 2 elements: the first and last profile to fetch. For instance, `ArgoSet = DataFetcher().profile(6902746,[1,34])` will fetch all data from cycle 1 to 34 (again for more experienced users).

### III.5 - User modes: level of details in the outputs, quality and level of processing considered
The argo files are very rich, containing a lot of information, which can be difficult to manipulate, especially for people not implied in the data management process. To simplify and provide data ready for studies and analysis, the argoPy embeds a nice *user mode* selection possibility, which is detailed [here](https://argopy.readthedocs.io/en/latest/user-guide/fetching-argo-data/user_mode.html).
In the ENVRI-Hub context, recommended modes are either "standard" (default configuration) or "research" modes. Briefly, standard mode contains the best possible good data (both real-time data and expert-reviewed data), while research mode only contains good data that were expert-reviewed. 
+ `argopy.set_options(mode='standard')`
+ `argopy.set_options(mode='research')`
  
### III.6 - output formating
Data can be output in several format such as dataframes or datasets:
+ `DataFetcher().profile(6902746, 34).to_dataframe()`
+ `DataFetcher().profile(6902746, 34).to_xarray()`

# ENVRI HUB library usage
