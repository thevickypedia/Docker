docker-compose up -d
python3 run_tests.py RUN_TEST
docker-compose down
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q) -f