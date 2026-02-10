<!-- vscode-markdown-toc -->
- [ECVs, ENVRI-HUB](#ecvs-envri-hub)
- [beacon](#beacon)
  - [docker compose](#docker-compose)
  - [api/info](#apiinfo)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

# ECVs, ENVRI-HUB



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
