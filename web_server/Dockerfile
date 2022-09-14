FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN mkdir /usr/bin/web_server
RUN mkdir /usr/bin/web_server/views
COPY web_server/python_web_server/main.py /usr/bin/web_server/
COPY web_server/python_web_server/views/index.php /usr/bin/web_server/views/
CMD [ "python3", " /usr/bin/web_server/main.py"]