<!-- vscode-markdown-toc -->
- [ECVs, ENVRI-HUB](#ecvs-envri-hub)
- [Template cell](#template-cell)
  - [param cell](#param-cell)
  - [exec cell](#exec-cell)
- [beacon](#beacon)
  - [docker compose](#docker-compose)
  - [api/info](#apiinfo)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

# ECVs, ENVRI-HUB

# Template cell

## <a name='paramcell'></a>param cell

```python
# DO NOT CONTAINERISE
# =====
# Dependency
# -----
# ! pip install -r requirements.txt
# ! pip list
# ! conda list

import os
import sys
from datetime import datetime

# base settings
# -----
conf_vlab_name     = "ECVs"
conf_workflow_name = "AnaEE"

# conf_workflow_id = f"wid-{datetime.now().strftime('%Y%m%d_%H%M%S%f')}"
param_workflow_name = f"wid-{datetime.now().strftime('%Y%m%d_%H%M%S%f')}"

# dev
# -----
# library: --volume="//c/DockerShare/ECVs:/home/jovyan" naavre-fl-ecvs-jupyter:local
# NaaVRE: /home/jovyan/Virtual Labs/ECVs/Git public
# dir_code = os.path.join("/", "home", "jovyan", "Virtual Labs")
# if not os.path.exists(dir_code):
#     os.makedirs(dir_code)

# dir_data = os.path.join("/", "home", "jovyan", "Cloud Storage", "naa-vre-user-data")
# if not os.path.exists(dir_data):
#     os.makedirs(dir_data)

# conf_dir_code  = os.path.join(dir_code, "ECVs", "Git public", "library")
# conf_dir_data  = os.path.join(dir_data, "ECVs", param_workflow_name)
# conf_dir_param = os.path.join(dir_data, "ECVs", param_workflow_name)

# local
# -----
conf_dir_workspace = os.path.join("/", "home", "jovyan", "Cloud Storage")

conf_dir_data_local_tmp = os.path.join("/", "tmp", "data")

# MINIO
# -----
conf_minio_public_bucket      = "naa-vre-public"
conf_minio_public_bucket_root = f"vl-{conf_vlab_name.lower()}"
conf_minio_public_local_root  = os.path.join(conf_dir_workspace, conf_minio_public_bucket, conf_minio_public_bucket_root)
conf_minio_public_local_code  = os.path.join(conf_dir_workspace, conf_minio_public_bucket, conf_minio_public_bucket_root, "code")
conf_minio_public_local_data  = os.path.join(conf_dir_workspace, conf_minio_public_bucket, conf_minio_public_bucket_root, "data", conf_workflow_name)

conf_minio_user_bucket        = "naa-vre-user-data"
# conf_minio_user_bucket_root   = param_user_email
conf_minio_user_bucket_root   = conf_vlab_name
conf_minio_user_local_root    = os.path.join(conf_dir_workspace, conf_minio_user_bucket,   conf_minio_user_bucket_root)
conf_minio_user_local_code    = os.path.join(conf_dir_workspace, conf_minio_user_bucket,   conf_minio_user_bucket_root,   "library")
conf_minio_user_local_data    = os.path.join(conf_dir_workspace, conf_minio_user_bucket,   conf_minio_user_bucket_root,   f"{conf_workflow_name}-{param_workflow_name}")
conf_minio_user_local_flog    = os.path.join(conf_minio_user_local_data, "log.md")

# API key
# -----
# If running under NaaVRE, input `your api key` with the correct value and input in the GUI:
secret_SERVICE_KEY = "d18e08911c964d45912eb1e954adf994"
# secret_SERVICE_KEY = SecretsProvider().set_secret("secret_SERVICE_KEY")
# secret_SERVICE_KEY = SecretsProvider().get_secret("secret_SERVICE_KEY")

# Input param
# -----
# CREA AA Italian historical weather series
# https://api.anaee.eu/crea-aa-dailymeteo/
conf_SERVICE_URL_CREA    = 'https://api.anaee.eu/crea-aa-dailymeteo'
conf_SERVICE_METHOD_CREA = "POST"

# An API to access CREA's mirror of the Copernicus ERA5 dataset
# https://api.anaee.eu/era5-data-access
conf_SERVICE_URL_ERA5    = 'https://api.anaee.eu/era5-data-access'
conf_SERVICE_METHOD_ERA5 = "POST"

# param_polygon_string = ""
param_polygon_string = "" \
"POLYGON(" \
    "(" \
    "10.15905865446625 43.58782080564057," \
    "10.20849713102875 44.29581102576821," \
    "9.23071392790375 44.73060761735282," \
    "7.709107482591251 44.45678937969159," \
    "7.385010802903751 43.72294797699299," \
    "10.15905865446625 43.58782080564057" \
    ")" \
")"

param_crea_request_getStationData    = "getStationData"
param_crea_start_date_getStationData = "2022-06-14"
param_crea_end_date_getStationData   = "2022-06-20"
param_crea_timestep_getStationData   = "hour"
# input_crea_data_getStationData = {
#     "startTime": param_crea_start_date_getStationData,
#     "endTime":   param_crea_end_date_getStationData,
#     "timeStep":  param_crea_timestep_getStationData,
#     "wkt":       param_polygon_string
# }

param_crea_request_getRasterData    = "getRasterData"
param_crea_start_date_getRasterData = "2002-06-14"
param_crea_end_date_getRasterData   = "2002-06-20"
param_crea_timestep_getRasterData   = "day"
# input_crea_data_getRasterData = {
#     "startTime": param_crea_start_date_getRasterData,
#     "endTime":   param_crea_end_date_getRasterData,
#     "timeStep":  param_crea_timestep_getRasterData,
#     "wkt":       param_polygon_string,
#     "group":     "sian"
# }

param_crea_request_getNearestStationData    = "getNearestStationData"
param_crea_start_date_getNearestStationData = "2021-06-14"
param_crea_end_date_getNearestStationData   = "2021-06-20"
param_crea_timestep_getNearestStationData   = "hour"
# conf_crea_data_getNearestStationData = {
#     "startTime": param_crea_start_date_getNearestStationData,
#     "endTime":   param_crea_end_date_getNearestStationData,
#     "timeStep":  param_crea_timestep_getNearestStationData,
#     "wkt":       "POINT(9.3 44.5)",
#     "limit":     1
# }

param_era5_request_GetEraData    = "GetEraData"
param_era5_start_date_GetEraData = "2022-06-14"
param_era5_end_date_GetEraData   = "2022-06-20"
param_era5_timestep_GetEraData   = "hour"
# input_era5_data_GetEraData = {
#     "startTime": param_era5_start_date_GetEraData,
#     "endTime":   param_era5_end_date_GetEraData,
#     "timeStep":  param_era5_timestep_GetEraData,
#     "wkt":       param_polygon_string
# }

print("Finish: NaaVRE parameters")
print(f"Workspace public:")
print(f"  Root: {conf_minio_public_local_root}")
print(f"  Code: {conf_minio_public_local_code}")
print(f"  Data: {conf_minio_public_local_data}")

print(f"Workspace user:")
print(f"  Root: {conf_minio_user_local_root}")
print(f"  Code: {conf_minio_user_local_code}")
print(f"  Data: {conf_minio_user_local_data}")
print(f"  Log:  {conf_minio_user_local_flog}")

# func_call_restful_api = anaee_api.call_restful_api()
# func_parse_wkt_point  = anaee_api.parse_wkt_point()

```

## <a name='execcell'></a>exec cell

```python
# ECVs, workflow start
# ---
# NaaVRE:
#  cell:
#   outputs:
#    - dummy_cell_arg_o: String
# ...

import os
import sys
from datetime import datetime

# sys.path.append(conf_minio_public_local_code)
# sys.path.append(conf_minio_user_local_code)

# prepare folders
# .....
if not os.path.exists(conf_dir_data_local_tmp):
    os.makedirs(conf_dir_data_local_tmp)

# if not os.path.exists(conf_minio_public_local_root):
#     os.makedirs(conf_minio_public_local_root)

if not os.path.exists(conf_minio_user_local_root):
    os.makedirs(conf_minio_user_local_root)

if not os.path.exists(conf_minio_user_local_data):
    os.makedirs(conf_minio_user_local_data)
    
with open(conf_minio_user_local_flog, "w+") as fp_log:
    fp_log.write(f"# {param_workflow_name}\n")

# create log
# .....
workflow_step = "ECVs-Start"

if os.path.exists(conf_minio_user_local_flog):
    with open(conf_minio_user_local_flog, "a+") as fp_log:
        fp_log.write(f"\n## {workflow_step}\n") 
else:
    if not os.path.exists(conf_minio_user_local_data):
        os.makedirs(conf_minio_user_local_data)
    with open(conf_minio_user_local_flog, "w+") as fp_log:
        fp_log.write(f"\n## {workflow_step}\n") 

# lib
# -----

# input
# -----
dummy_cell_arg_i = "dummy input"

# output
# -----
dummy_cell_arg_o = "dummy output"

# func
# -----

# start
# -----

# -----
with open(conf_minio_user_local_flog, "a+") as fp_log:
    fp_log.write(f"\nFinish: {workflow_step}\n")
    fp_log.write(f"\nOutput: {conf_minio_user_local_data}\n")

print(f"Finish: {workflow_step}")
```

# <a name='beacon'></a>beacon

Data lake query engine 

* [beacon, MARIS](https://beacon.maris.nl/)
* [beacon, github](https://github.com/maris-development/beacon)
* [beacon, Docs](https://maris-development.github.io/beacon/)
* [Rust, shell](https://sh.rustup.rs)

## <a name='dockercompose'></a>docker compose

```shell
docker system prune -f

cd C:\DockerShare\ECVs
docker compose up
# docker compose up -d

docker compose ps

docker exec -it beacon bash
cd /beacon/data

docker compose down
```

## <a name='apiinfo'></a>api/info

Curl

```shell
curl -X 'GET' \
  'http://localhost:8080/api/info' \
  -H 'accept: */*'
```

Request URL

```shell
http://localhost:8080/api/info
```
