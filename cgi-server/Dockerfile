FROM httpd
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
ADD ./cgi /usr/local/apache2/cgi-bin
RUN apt update && apt upgrade -y && apt install python3 subversion -y && apt install python3-pip -y && pip3 install mcrcon requests2 pyyaml && cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime && chmod 755 -R /usr/local/apache2/cgi-bin && cd /usr/local/apache2/cgi-bin && rm printenv printenv.vbs printenv.wsf test-cgi
