# Instructions for testing/developing with Docker

## Install Docker
[Docker for Windows](https://docs.docker.com/docker-for-windows/install/)

## Build 
```
$ cd ChristmasLister
$ docker image build -t christmastlister:latest .
```
## Run
```
$ docker container run -d -p 8000:8000 --rm --name christmaslister christmastlister:latest
```

After the docker image is build and a container is running. You can navigate to [http://localhost:8000](http://localhost:8000)

