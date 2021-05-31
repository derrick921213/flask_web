# Set base workdir
tar -zcvf server.tar.gz docker
mv server.tar.gz flask-server
basedir=$(dirname "$0")
cgi=$basedir/cgi-server
flask=$basedir/flask-server
mc=$basedir/minecraft-server

# Build custom image.
docker build -t flask-server "$flask" --no-cache
docker build -t cgi-server "$cgi" --no-cache
docker build -t mc-server "$mc" --no-cache

# Stop the container created before
docker stop flask-test cgi-test mc-test
docker network create service
#Run docker container.
cd $mc
docker run -d --rm -p 25565:25565 -p 25575:25575 --name mc-test -v $PWD:/mcserver -v /mcserver/logs --name=mc-test --network service --network-alias mc-test mc-server
cd logs
rm *.log.gz
docker run -d --rm -p 8081:80 --name cgi-test --volumes-from mc-test --name=cgi-test --network service --network-alias cgi-test cgi-server
docker run -d --rm -p 80:5000 --name flask-test --network service --network-alias flask-test flask-server
