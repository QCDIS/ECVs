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

conf_workflow_id = f"wid-{datetime.now().strftime('%Y%m%d_%H%M%S%f')}"

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

# local
# -----
conf_dir_workspace = os.path.join("/", "home", "jovyan", "Cloud Storage")

conf_dir_data_local_tmp = os.path.join("/", "tmp", "data")
if not os.path.exists(conf_dir_data_local_tmp):
    os.makedirs(conf_dir_data_local_tmp)

# MINIO
# -----
conf_minio_public_bucket      = "naa-vre-public"
conf_minio_public_bucket_root = f"vl-{conf_vlab_name.lower()}"
conf_minio_public_local_root  = os.path.join(conf_dir_workspace, conf_minio_public_bucket, conf_minio_public_bucket_root)
conf_minio_public_local_code  = os.path.join(conf_dir_workspace, conf_minio_public_bucket, conf_minio_public_bucket_root, "code")
conf_minio_public_local_data  = os.path.join(conf_dir_workspace, conf_minio_public_bucket, conf_minio_public_bucket_root, "data", conf_workflow_name)
# if not os.path.exists(conf_minio_public_local_root):
#     os.makedirs(conf_minio_public_local_root)

conf_minio_user_bucket        = "naa-vre-user-data"
# conf_minio_user_bucket_root   = param_user_email
conf_minio_user_bucket_root   = conf_vlab_name
conf_minio_user_local_root    = os.path.join(conf_dir_workspace, conf_minio_user_bucket,   conf_minio_user_bucket_root)
conf_minio_user_local_code    = os.path.join(conf_dir_workspace, conf_minio_user_bucket,   conf_minio_user_bucket_root,   "library")
conf_minio_user_local_data    = os.path.join(conf_dir_workspace, conf_minio_user_bucket,   conf_minio_user_bucket_root,   f"{conf_workflow_name}-{conf_workflow_id}")
conf_minio_user_local_flog    = os.path.join(conf_minio_user_local_data, "log.md")
if not os.path.exists(conf_minio_user_local_root):
    os.makedirs(conf_minio_user_local_root)

if not os.path.exists(conf_minio_user_local_data):
    os.makedirs(conf_minio_user_local_data)
with open(conf_minio_user_local_flog, "w+") as fp_log:
    fp_log.write(f"# {conf_workflow_id}\n") 

# API key
# -----
# If running under NaaVRE, input `your api key` with the correct value and input in the GUI:
secret_SERVICE_KEY = ""
# secret_SERVICE_KEY = SecretsProvider().set_secret("secret_SERVICE_KEY")
# secret_SERVICE_KEY = SecretsProvider().get_secret("secret_SERVICE_KEY")

# Input param
# -----
conf_args = ""

param_variable = ""

print("Finish: NaaVRE parameters")
print(f"Workspace public: {conf_minio_public_local_root}")
print(f"  {conf_minio_public_local_code}")
print(f"  {conf_minio_public_local_data}")

print(f"Workspace user: {conf_minio_user_local_root}")
print(f"  {conf_minio_user_local_code}")
print(f"  {conf_minio_user_local_data}")
print(f"  {conf_minio_user_local_flog}")

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
    fp_log.write(f"\nOutput: {file_seq_zip}\n")

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
