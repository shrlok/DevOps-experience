FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN mkdir -p /usr/bin/web_server/views

COPY ./python_web_server/* /usr/bin/web_server/

EXPOSE 8080/tcp
CMD python3 /usr/bin/web_server/main.py

HEALTHCHECK --interval=5m --timeout=5s CMD curl -f http://127.0.0.1/index.html || exit 1