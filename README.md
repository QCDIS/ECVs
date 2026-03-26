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

