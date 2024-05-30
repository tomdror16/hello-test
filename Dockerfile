# Docker file python hello app

FROM centos:7

EXPOSE 80
EXPOSE 8080

RUN yum update -y && \
    yum install -y python3 && \
    yum clean all && \ 
    rm -rf /var/cache/yum

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./hello.py hello.py

CMD [ "python3","hello.py" ]


