docker rm batchvalidator
#docker run -d  -p 5000:5000 --name batchvalidator batchvalidator /app/run_server.sh
docker run -it -p 5020:5000 --name batchvalidator batchvalidator /app/run_server.sh
