#The image is based on httpd
FROM httpd
# update software and install python3 & pip
RUN apt update && apt upgrade -y && apt install net-tools iputils-ping -y && apt install python3 -y && apt install python3-pip -y
#Set workdir
WORKDIR /MCcontroler
RUN cd /MCcontroler
RUN cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime
ADD server.tar.gz /MCcontroler
EXPOSE 5000
RUN pip3 install flask flask_login flask_sqlalchemy flask_jwt_extended 
CMD ["python3","/MCcontroler/docker/main.py"] 