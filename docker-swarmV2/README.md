# Gitlab HA deployed on Swarm

In this project you can find the deployment files necessary to deploy a high availability Gitlab on a Docker Swarm.

It is important to mention that there is little to no support for deploying Gitlab in a swarm configuration.

## Requirements

In order to deploy a Gitlab service using docker swarm you need to have
a docker swarm available and a NFS server.

The NFS server will serve as volumes to the docker images.
It also allows for the Gitlab image to be distributed correctly.

Most of the inspiration came from [1], it is a very complete guide. The deployment here expands the original idea by providing HA PostgreSQL, Redis, Grafana and updating all the versions of the components.

## Access to the Swarm

This part is only relevant when connecting to the swarm available on the department.

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

The docker swarm has currently three managers:

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

We also deployed a personal docker swarm for development.
This small swarm is compose by one manager and three workers.

To use the local swarm run the following command:

```bash
export DOCKER_HOST="ssh://ubuntu@192.168.85.218"
```

## NFS Server

The NFS server is in srv2-deti.
The storage will be accessed at full speed if the containers are running in srv2-deti (compute2XX),
but will be limited to 100Mbits/s if the containers are running at srv1 or srv4.

You can mount the share in your laptop by issuing:

```bash
sudo mkdir -p /mnt/nfs
sudo mount -t nfs4 srv2-deti.ua.pt:/mnt/nfs /mnt/nfs
```

For the local deployment at IT use the following commands:

```bash
sudo mkdir -p /mnt/nfs
sudo mount -t nfs4 192.168.85.141:/mnt/nfs /mnt/nfs
```

## Deploy the service

The project will use the following ports: 5100-5199

Create an overlay network for your services.
It will be used to expose the services to the public network.

```bash
docker network create --driver overlay gitlab_p2
```

Configure the NFS folder for the gitlab service.
Mount the NFS system in your local machine using the commands in [NFS server](#NFS-server).
After mounting the NFS, run the following commands:

```bash
sudo mkdir -p /mnt/nfs/gitlab_p2/gitlab/{data,config}
sudo mkdir -p /mnt/nfs/gitlab_p2/pg/{pg0,pg1}
sudo mkdir -p /mnt/nfs/gitlab_p2/prometheus
sudo chmod -R 2777 /mnt/nfs/gitlab_p2/
```

After that deploy the PostgreSQL cluster stack:

```bash
docker stack deploy -c pg.yml p2_pg
```

And connect to it to create the necessary missing databases (the password is adminpassword):

```bash
psql -h 10.4.0.1 -p 5154 -U postgres -W
create user gitlab;
create database gitlab;
grant all ON DATABASE gitlab TO gitlab;
create database grafana;
grant all ON DATABASE grafana TO gitlab;
\q
```

Drop the previous stack and launch the stack with the gitlab services:

```bash
docker stack rm p2_pg
docker stack deploy -c stack.yml p2_gitlab
```

Add swarm.local to the /etc/hosts file. It is the host that traefik is expecting.

```bash
sudo nano /etc/hosts
```

For DETI swarm paste:

```
10.2.0.1 swarm.local
```

For IT swarm paste:

```
192.168.85.218 swarm.local
```

After that the service is completely accessible.

1. Grafana - http://swarm.local:5100/grafana
2. Prometheus - http://swarm.local:5100/prometheus
3. Gitlab - http://swarm.local:5180
4. Traefik dashboard - http://swarm.local:5188

## References

1. [Deploying gitlab on Docker Swarm](https://dev.to/livioribeiro/deploying-gitlab-on-docker-swarm-1fb1)