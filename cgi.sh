# Set base workdir
basedir=$(dirname "$0")
cgi=$basedir/cgi-server
# Build custom image.
docker build -t cgi-server "$cgi"
# Stop the container created before
docker stop cgi-test
#Run docker container.

docker run -d --rm -p 8081:80 --name cgi-test --volumes-from mc-test --name=cgi-test --network service --network-alias cgi-test cgi-server
