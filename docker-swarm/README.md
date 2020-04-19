# Deploy Gitlab with Docker Swarm

This README.md contains notes and relevant links that were used in the development of the project


## Requirements

In order to deploy a Gitlab service using docker swarm you need to have a swarm available and a NFS server.

The NFS server will serve as volumes to the docker images. It also allows for the Gitlab image to be distributed correctly.

Most of the inspiration came from [1], it is a very complete guide.

## Create a docker swam

## Create a NFS server

## Deploy the service

The tips and trick written where were made for the ATNoG swarm cluster.

Export the following variable, this way your local docker CLI will issue commands to the remote docker server:

```bash
export DOCKER_HOST=ssh://ubuntu@192.168.85.218
```

Create an overlay network for your services.
It will also be use by the reverse proxy/load balancer to communicate with the other services:

```bash
docker network create --driver overlay proxy
```

Firs deploy the reverser proxy/load balancer:

```bash
docker stack deploy -c traefik.yml traefik
``` 

After that deploy the gitlab stack:

```bash
docker stack deploy -c stack.yml gitlab
``` 

## References

1. [Deploying gitlab on Docker Swarm](https://dev.to/livioribeiro/deploying-gitlab-on-docker-swarm-1fb1)

2. [How to install Traefik 2.x on a Docker Swarm](https://blog.creekorful.com/how-to-install-traefik-2-docker-swarm/)

3. [Integrate Traefik 2.1 Reverse Proxy with Docker Swarm Services](https://medium.com/better-programming/traefik-2-1-as-a-reverse-proxy-c9e274da0a32)