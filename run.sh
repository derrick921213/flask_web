# Set base workdir
tar -zcvf server.tar.gz docker
mv server.tar.gz flask-server
basedir=$(dirname "$0")
cgi=$basedir/cgi-server
flask=$basedir/flask-server
# Build custom image.
docker build -t flask-server "$flask"
docker build -t cgi-server "$basedir2"
# Stop the container created before
docker stop flask-test cgi-test
cd $basedir/docker/website/cgi
#Run docker container.
docker run -d --rm -p 8081:80 --name cgi-test -v $PWD:/usr/local/apache2/cgi-bin/ cgi-server
docker run -d --rm -p 5000:5000 --name flask-test flask-server
