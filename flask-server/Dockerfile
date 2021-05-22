#The image is based on httpd
FROM httpd
# update software and install python3 & pip
RUN apt update && apt upgrade -y && apt install net-tools -y && apt install python3 -y && apt install python3-pip -y
#Set workdir
WORKDIR /MCcontroler
RUN cd /MCcontroler
ADD server.tar.gz /MCcontroler
EXPOSE 5000
RUN pip3 install flask flask_login flask_sqlalchemy
CMD ["python3","/MCcontroler/docker/main.py"] 