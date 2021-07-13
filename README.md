# Docker
Dockerfiles to test out different docker functions.

<details>
<summary>Docker Helper Commands</summary>

###### Docker Build
```bash
docker build -t test .
```
###### Docker Run
```bash
docker run test
```
###### Docker compose
[`docker-compose up`](https://docs.docker.com/compose/reference/up/)
###### Docker List all Containers
```bash
docker ps -a -q
```
###### Docker Stop
```bash
docker stop <CONTAINER_ID>
```
###### Docker Remove Container
```bash
docker rm <CONTAINER_ID>
```
###### Docker Remove Images
```bash
docker rmi $(docker images -q) -f
```
###### Docker Cleanup
```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q) -f
```
</details>
