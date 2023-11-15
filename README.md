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
Clean up a single Image/Container
```bash
docker stop $(docker ps -aqf "ancestor=<IMAGE NAME>")
docker rm $(docker ps -aqf "ancestor=<IMAGE NAME>")
docker rmi $(docker ps -aqf "ancestor=<IMAGE NAME>") -f
[OR]
docker stop $(docker ps -aqf "name=^<CONTAINER NAME>$")
docker rm $(docker ps -aqf "name=^<CONTAINER NAME>$")
docker rmi $(docker ps -aqf "name=^<CONTAINER NAME>$") -f
```
[Options](https://docs.docker.com/engine/reference/commandline/ps/)
```text
-q: for quiet. output only the ID
-a: for all. works even if your container is not running
-f: for filter.
^: Container name must start with this string
$: Container name must end with this string
```
<br>

Clean up all the Images/Containers
```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q) -f
docker builder prune
```

Alias for docker cleanup
```shell
alias clean-docker='function _clean_docker() { \
    clear; \
    echo "*****************************************************************************************************************"; \
    echo "*****************************************************************************************************************"; \
    echo ""; \
    echo "The following containers and their images will be removed."; \
    echo ""; \
    echo "$(docker ps -a)"; \
    echo ""; \
    echo "*****************************************************************************************************************"; \
    echo "*****************************************************************************************************************"; \
    read -r -p "Are you sure you want to continue? <Y/N> " prompt; \
    if [[ $prompt =~ [yY](es)* ]]; then \
        docker stop $(docker ps -a -q); \
        docker rm $(docker ps -a -q); \
        docker rmi $(docker images -q) -f; \
        docker builder prune; \
    else \
        echo ""; \
        echo "***************************************************************************************************************"; \
        echo "Deletion cancelled"; \
        echo "***************************************************************************************************************"; \
    fi; \
}; _clean_docker'
```
</details>
