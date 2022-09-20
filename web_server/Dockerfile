FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
#for test
RUN apt install net-tools vim curl -y
#
RUN mkdir -p /usr/local/bin/web_server/views

COPY ./python_web_server/main.py /usr/local/bin/web_server/
COPY ./python_web_server/views/* /usr/local/bin/web_server/views/

EXPOSE 8086/tcp

WORKDIR /usr/local/bin/web_server/
CMD ["python3", "/usr/local/bin/web_server/main.py"]

HEALTHCHECK --interval=5m --timeout=5s CMD curl -f http://127.0.0.1:8086/index.html || exit 1
