# Deploying Simple Python application on a Docker container
This guide will go through how to deploy a simple Python Flask App on a docker container and how to validate it.

## Prerequists
Please install docker engine. This example uses Centos7. Any other linux flavor should work.
Docker can be installed using. https://docs.docker.com/engine/install/centos/

## Build and Deploy
### Clone the repository
```git clone https://github.com/fcam-naveen/hello-world.git ```\
```cd hello-world ```

### Build Docker image
```docker build -t hello-app:latest . ```
This will build docker image ```hello-app``` and check docker image using ```docker images```

### Deploy your application
```docker run -d -p 8080:8080 --name simple_hello_app -it hello-app ```

## Verification
http://localhost:8080 should return ```Hello!```  and \
http://localhost:8080/healthz should return
```
{
  "status": "OK",
  "version": "0.0.1",
  "uptime": "up since 2020-12-28 05:50:28"
}
```

### Debugging
If browser return any failure, please make sure docker container is running.
You can check using ```docker ps -a```. If the container STATUS is not Up, you can run ```docker logs simple_hello_app``` to check errors.
# hello-test
