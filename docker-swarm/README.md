# Deploy Gitlab with Docker Swarm

This README.md contains the necessary steps to deploy a high availability gitlab platform.
The platform is deployed in a cluster of docker swarm machines.
Furthermore, we include notes and relevant links that were used in the development of the project


## Requirements

In order to deploy a Gitlab service using docker swarm you need to have
a docker swarm available and a NFS server.

The NFS server will serve as volumes to the docker images.
It also allows for the Gitlab image to be distributed correctly.

Most of the inspiration came from [1], it is a very complete guide.

## VPN access

The docker swarm and NFS are available through two VPNs:

1. [UA Check Point VPN](https://go.ua.pt/)
2. DETI OpenVPN

After connecting to the two VPNs, in the correct order,
you can access the machines were the project was deployed.

### UA Check Point VPN

Run the following command to connect:

```bash
snx
```

Run the following command to disconnect:

```bash
snx -d
```

### DETI OpenVPN

Run the following command to connect:

```bash
cd ~/.vpn/DETI_VPN/
./start.sh
```

## Docker Swarm

The docker swarm has currently three managers

1. 10.1.0.1
2. 10.2.0.1
3. 10.4.0.1 

There is a [swarmpit](https://swarmpit.io/) dashboard available:

| URL      | [http://10.2.0.1:888/](http://10.2.0.1:888/) |
|----------|----------------------------------------------|
| User     | user |
| Password | user |

In order to use them in your local computer just export the following variable,
this way your local docker CLI will issue commands to the remote docker server:

```bash
export DOCKER_HOST="tcp://10.2.0.1:2375"
```

## NFS server

The NFS server is in srv2-deti.
The storage will be accessed at full speed if the containers are running in srv2-deti (compute2XX),
but will be limited to 100Mbits/s if the containers are running at srv1 or srv4.

You can mount the share in your laptop by issuing: sudo mount srv2-deti.ua.pt:

```bash
sudo mkdir -p /mnt/nfs
sudo mount -t nfs srv2-deti.ua.pt:/mnt/nfs /mnt/nfs
```

## Deploy the service

The project will use the following ports: 5100-5199

Create an overlay network for your services.
It will also be use by the reverse proxy/load balancer to communicate with the other services:

```bash
docker network create --driver overlay gitlab_p2
```

Configure the NFS folder for the gitlab service.
Mount the NFS system in your local machine using the commands in [NFS server](#NFS-server).
After mounting the NFS, run the following commands:

```bash
sudo mkdir -p /mnt/nfs/gitlab_p2/gitlab/{data,logs,config}
sudo mkdir -p /mnt/nfs/gitlab_p2/postgres
sudo mkdir -p /mnt/nfs/gitlab_p2/grafana
sudo mkdir -p /mnt/nfs/gitlab_p2/prometheus
sudo chmod -R 777 /mnt/nfs/gitlab_p2/
```

After that deploy the gitlab stack:

```bash
docker stack deploy -c stack.yml gitlab
```

## TODO Load Balancer and Proxy:

First deploy the reverser proxy/load balancer:

```bash
docker stack deploy -c traefik.yml traefik
``` 

## Docker Reference

1. List all the nodes: `docker node ls`
2. List all networks: `docker network ls`

## References

1. [Deploying gitlab on Docker Swarm](https://dev.to/livioribeiro/deploying-gitlab-on-docker-swarm-1fb1)

2. [How to install Traefik 2.x on a Docker Swarm](https://blog.creekorful.com/how-to-install-traefik-2-docker-swarm/)

3. [Integrate Traefik 2.1 Reverse Proxy with Docker Swarm Services](https://medium.com/better-programming/traefik-2-1-as-a-reverse-proxy-c9e274da0a32)


## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details