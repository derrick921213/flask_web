FROM httpd
RUN apt update && apt upgrade -y && apt install net-tools -y && apt install python3 -y && apt install python3-pip -y
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
RUN chown 755 -R /usr/local/apache2/cgi-bin