FROM httpd
RUN apt update && apt upgrade -y && apt install net-tools -y && apt install python3 -y && apt install python3-pip -y
RUN pip3 install mcrcon
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
ADD ./cgi /usr/local/apache2/cgi-bin
RUN chmod 755 -R /usr/local/apache2/cgi-bin
RUN cd /usr/local/apache2/cgi-bin && rm printenv printenv.vbs printenv.wsf test-cgi