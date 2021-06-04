#The image is based on httpd
FROM httpd
#Set workdir
ADD server.tar.gz /MCcontroler
WORKDIR /MCcontroler
RUN apt update && apt install python3 -y && apt install python3-pip -y && pip3 install flask flask_login flask_sqlalchemy flask_jwt_extended pyyaml
EXPOSE 5000
CMD ["python3","/MCcontroler/docker/main.py"] 