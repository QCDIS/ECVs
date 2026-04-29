## AnaEE

Analysis and Experimentation on Ecosystems, [API](https://developer.anaee.eu/apis)

### getNearestStationData

Example output:

| date | seriesID | averageTemp | precipitation | idGroup | idCode | stationName | country | elevation | geography |
| ---- | -------- | ----------- | ------------- | ------- | ------ | ----------- | ------- | --------- | --------- |
| 2022-06-14 00:00:00+02:00 | 11 | 13.5 | 0.0 | regione-liguria | CABAN | Cabanne | IT | 809.0 | POINT (9.3408 44.4883) |


### getStationData

Example output:

| date | seriesID | averageTemp | maxTemp | minTemp | windSpeed | maxWindSpeed | windGust | precipitation | stationPressure | RHMin | RHMax | RAD | leafWetness | idGroup | idCode | stationName | country | elevation |
| ---- | -------- | ----------- | ------- | ------- | --------- | ------------ | -------- | ------------- | --------------- | ----- | ----- | --- | ----------- | ------- | ------ | ----------- | ------- | --------- |
| 2022-06-14 00:00:00+02:00 | 11 | NaN | NaN | NaN | NaN | NaN | 0.0 | NaN | NaN | NaN | NaN | NaN | regione-liguria | AGORR | Alpe Gorreto | IT | 915.0 |
    

### getRasterData

Example output:

| date | seriesID | averageTemp | maxTemp | minTemp | windSpeed | maxWindSpeed | windGust | precipitation | stationPressure | RHMin | RHMax | RAD | leafWetness | idGroup | idCode | stationName | country | elevation |
| ---- | -------- | ----------- | ------- | ------- | --------- | ------------ | -------- | ------------- | --------------- | ----- | ----- | --- | ----------- | ------- | ------ | ----------- | ------- | --------- |
| 2022-06-14 00:00:00+02:00 | 11 | NaN | NaN | NaN | NaN | NaN | 0.0 | NaN | NaN | NaN | NaN | NaN | regione-liguria | AGORR | Alpe Gorreto | IT | 915.0 |


### GetEraData

Example output:

| station_id | idGroup | Country | firstRecord | lastRecord | Elevation | Latitude | Longitude | nuts1 | nuts2 | nuts3 | geometry | Date | date_index | d2m | t2m | u10 | v10 | ssrd | tp | rh | windspeed |
| ---------- | ------- | ------- | ----------- | ---------- | --------- | -------- | --------- | ----- | ----- | ----- | -------- | ---- | ---------- | --- | --- | --- | --- | ---- | -- | -- | --------- | 
| 9.50-44.25 | Era5 | Italia | 1900-01-01 00:00:00+00:00 | 2024-09-18 23:00:00+00:00 | 268.46797089999995 | 44.25 | 9.5 | Nord-Ovest | Liguria | Genova | POINT(9.5 44.25) | 2022-06-15 00:00:00+00:00 | 2022-06-15 00:00:00+00:00 | 19.75967612471516 | 24.44530128934332 | -1.9472449479938327 | -2.374912076563004 | -2.3283064365386963e-10 | 0.0 | 0.751407767589943 | 3.071151292087758 |


## ARGO

Real-time global ocean in situ observing system, [Data access](https://www.euro-argo.eu/Argo-Data-access)

Example output:

erddap, phy, standard
* PRES: Sea Pressure
* PSAL: PRACTICAL SALINITY
* TEMP: SEA TEMPERATURE IN SITU ITS-90 SCALE

### Source

* `erddap`: the Ifremer erddap server (Default)
* `gdac`: an Argo GDAC server or any other GDAC-compliant local folder
* `argovis`: the Argovis server

### Dataset

* `phy`: physical parameters
* `bgc`: biogeochemical parameters

## Test

### List variables

```python
# DO NOT CONTAINERISE
# =====
# Test only

!pip install beacon-api

from beacon_api import Client

file_variable_csv = os.path.join(conf_minio_user_local_data, "variable_list.csv")

with open(file_variable_csv, "w+") as fp_csv:
    # conf_SERVICE_URL_BEACON_NODE_ACTRIS = "https://beacon-iriscc.maris.nl"  # TODO, check url
    # conf_SERVICE_URL_BEACON_NODE_ARGO   = "https://beacon-argo.maris.nl"    # jwt_token=BEACON_TOKEN
    # conf_SERVICE_URL_BEACON_NODE_CDI    = "https://beacon-cdi.maris.nl"     # jwt_token=BEACON_TOKEN
    # conf_SERVICE_URL_BEACON_NODE_IAGOS  = "https://beacon-iriscc.maris.nl"  # TODO, check url
    # conf_SERVICE_URL_BEACON_NODE_ICOS   = "https://beacon-iriscc.maris.nl"  # TODO, check url
    # conf_SERVICE_URL_BEACON_NODE_IRISCC = "https://beacon-iriscc.maris.nl"

    fp_csv.write("RI,table,variable,type\n")
    
    # ACTRIS
    # .....
    ri_name = "ACTRIS"
    tb_name = ""
    
    client = Client(conf_SERVICE_URL_BEACON_NODE_ACTRIS)
    tables = client.list_tables()
    print(f"\n## {ri_name}: {conf_SERVICE_URL_BEACON_NODE_ACTRIS}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        print(f"  * {name}\n")

    tb_name = "default"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        # if table_field.name.endswith('.standard_name'):
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "actris"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "actris-in-situ"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "actris-nrt"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    
    # ARGO
    # .....
    ri_name = "ARGO"
    tb_name = ""

    client = Client(conf_SERVICE_URL_BEACON_NODE_ARGO, jwt_token=secret_SERVICE_KEY)
    tables = client.list_tables()
    print(f"\n## {ri_name}: {conf_SERVICE_URL_BEACON_NODE_ARGO}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        print(f"  * {name}\n")

    tb_name = "default"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "argo"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "argo_bgc"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "argo_core"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")


    # CDI
    # .....
    ri_name = "CDI"
    tb_name = ""

    client = Client(conf_SERVICE_URL_BEACON_NODE_CDI, jwt_token=secret_SERVICE_KEY)
    tables = client.list_tables()
    print(f"\n## {ri_name}: {conf_SERVICE_URL_BEACON_NODE_CDI}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        print(f"  * {name}\n")

    tb_name = "default"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    
    # IAGOS
    # .....
    ri_name = "IAGOS"
    tb_name = ""

    client = Client(conf_SERVICE_URL_BEACON_NODE_IAGOS)
    tables = client.list_tables()
    print(f"\n## {ri_name}: {conf_SERVICE_URL_BEACON_NODE_IAGOS}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        print(f"  * {name}\n")

    tb_name = "default"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "iagos-l1"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")
    
    tb_name = "iagos-l2"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")
    

    # ICOS
    # .....
    ri_name = "ICOS"
    tb_name = ""

    client = Client(conf_SERVICE_URL_BEACON_NODE_ICOS)
    tables = client.list_tables()
    print(f"\n## {ri_name}: {conf_SERVICE_URL_BEACON_NODE_ICOS}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        print(f"  * {name}\n")

    tb_name = "default"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")


    # IRISCC
    # .....
    ri_name = "IRISCC"
    tb_name = ""

    client = Client(conf_SERVICE_URL_BEACON_NODE_IRISCC)
    tables = client.list_tables()
    print(f"\n## {ri_name}: {conf_SERVICE_URL_BEACON_NODE_IRISCC}\n")
    for name, table in tables.items():
        # print("*  ", name, table.get_table_type(), table.get_table_description())
        print(f"  * {name}\n")

    tb_name = "default"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "iriscc-no2"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")

    tb_name = "iriscc-p10"
    table_default = tables[tb_name]
    table_schema = table_default.get_table_schema_arrow()
    print(f"\n### table {ri_name},{tb_name}\n")
    for table_field in table_schema:
        if "." in table_field.name \
            or "_qc"    in str.lower(table_field.name) \
            or "_flag"  in str.lower(table_field.name) \
            or "_type"  in str.lower(table_field.name) \
            or "_error" in str.lower(table_field.name):
            pass
        else:
            fp_csv.write(f"{ri_name},{tb_name},{table_field.name},{table_field.type}\n")
            # print(f"{table_field.name}: {table_field.type}")
```

### Get variable names in the table

```python
with open(conf_minio_user_local_flog, "a+") as fp_log:
    str_log = f"get variable names in {table_cdi} table"
    fp_log.write(f"\n## {str_log}\n")
    print(f"\n{str_log}")

    table_schema = tables[table_cdi].get_table_schema()

    std_cols = [col for col in table_schema.names if col.endswith('.standard_name')]

    query_builder = tables[table_cdi].query()

    for parameter in std_cols:
        query_builder.add_select_column(parameter)

    df_variable_names = query_builder.to_pandas_dataframe()

    str_log = df_variable_names.describe().to_string()
    fp_log.write(f"\n{str_log}\n")
    # print(f"\n{str_log}")
```