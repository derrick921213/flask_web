tar -zcvf server.tar.gz docker
mv server.tar.gz flask-server
basedir=$(dirname "$0")
flask=$basedir/flask-server
docker build -t flask-server "$flask"
docker stop flask-test
docker run -d --rm -p 80:5000 --name flask-test --network service --network-alias flask-test flask-server
