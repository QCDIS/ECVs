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

Example output:

erddap, phy, standard
* PRES: Sea Pressure
* PSAL: PRACTICAL SALINITY
* TEMP: SEA TEMPERATURE IN SITU ITS-90 SCALE

##### Source

* `erddap`: the Ifremer erddap server (Default)
* `gdac`: an Argo GDAC server or any other GDAC-compliant local folder
* `argovis`: the Argovis server

##### Dataset

* `phy`: physical parameters
* `bgc`: biogeochemical parameters

## Check variables

```python
# DO NOT CONTAINERISE
# =====

# conf_SERVICE_URL_BEACON_NODE_ARGO   = "https://beacon-argo.maris.nl"    # jwt_token=BEACON_TOKEN
# conf_SERVICE_URL_BEACON_NODE_CDI    = "https://beacon-cdi.maris.nl"     # jwt_token=BEACON_TOKEN
# conf_SERVICE_URL_BEACON_NODE_ICOS   = "https://beacon-iriscc.maris.nl"  # TODO, QPan, check
# conf_SERVICE_URL_BEACON_NODE_IRISCC = "https://beacon-iriscc.maris.nl"

with open(conf_minio_user_local_flog, "a+") as fp_log:

    # .....
    client = Client(conf_SERVICE_URL_BEACON_NODE_ARGO, jwt_token=secret_SERVICE_KEY)
    tables = client.list_tables()
    fp_log.write(f"\n* {conf_SERVICE_URL_BEACON_NODE_ARGO}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        fp_log.write(f"\n  * {name}\n")
        print(f"\n  * {name}")

    # table_default = tables["default"]
    # table_schema = table_default.get_table_schema_arrow()
    # fp_log.write(f"\n* table\n")
    # for table_field in table_schema:
    #     fp_log.write(f"\n  * {table_field.name}: {table_field.type}\n")
    #     # print(f"{table_field.name}: {table_field.type}")

    
    # .....
    client = Client(conf_SERVICE_URL_BEACON_NODE_CDI, jwt_token=secret_SERVICE_KEY)
    tables = client.list_tables()
    fp_log.write(f"\n* {conf_SERVICE_URL_BEACON_NODE_CDI}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        fp_log.write(f"\n  * {name}\n")
        print(f"\n  * {name}")

    # table_default = tables["default"]
    # table_schema = table_default.get_table_schema_arrow()
    # fp_log.write(f"\n* table\n")
    # for table_field in table_schema:
    #     fp_log.write(f"\n  * {table_field.name}: {table_field.type}\n")
    #     # print(f"{table_field.name}: {table_field.type}")

    
    # .....
    client = Client(conf_SERVICE_URL_BEACON_NODE_ICOS)
    tables = client.list_tables()
    fp_log.write(f"\n* {conf_SERVICE_URL_BEACON_NODE_ICOS}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        fp_log.write(f"\n  * {name}\n")
        print(f"\n  * {name}")

    # table_default = tables["default"]
    # table_schema = table_default.get_table_schema_arrow()
    # fp_log.write(f"\n* table\n")
    # for table_field in table_schema:
    #     fp_log.write(f"\n  * {table_field.name}: {table_field.type}\n")
    #     # print(f"{table_field.name}: {table_field.type}")

    
    # .....
    client = Client(conf_SERVICE_URL_BEACON_NODE_IRISCC)
    tables = client.list_tables()
    fp_log.write(f"\n* {conf_SERVICE_URL_BEACON_NODE_IRISCC}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        fp_log.write(f"\n  * {name}\n")
        print(f"\n  * {name}")

```