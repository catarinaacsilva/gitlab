# Deploy GitLab in a Docker swarm

You can easily configure and deploy your Docker-based GitLab installation in a swarm cluster.


## Requirements

- Ubuntu >=18.04
- Docker
- [Docker compose](https://docs.docker.com/compose/install/)
- Docker Swarm


## Install GitLab using docker-compose

1. Create a Docker-compose.yml : `cd dockerCompose`

2. Run `docker-compose up`



## Setup a Docker swarm

There are a few things that we will need before we can get to Gitlab:

- A proxy to forward the requests to the correct services
- Postgres and Redis
- Prometheus to collect metrics from Gitlab and Grafana to visualize these metrics
- An NFS4 share to store any persistent data we need

**The Proxy**

**Setting up NFS**

1. First we need to install the NFS server: `sudo apt install -y nfs-kernel-server` 
2. For the NFS share the will need a directory structure like the following:

```console
.
+-- /srv/gitlab-swarm/
|   +-- gitlab 
        +-- config
        +-- data
        +-- logs
|   +-- grafana     
|   +-- postgres
|   +-- prometheus
```

We can create it using the following shell:

```bash

mkdir -p /srv/gitlab-swarm && \
mkdir -p /srv/gitlab-swarm/gitlab/{data,logs,config} && \
mkdir -p /srv/gitlab-swarm/postgres && \
mkdir -p /srv/gitlab-swarm/grafana && \
mkdir -p /srv/gitlab-swarm/prometheus && \
chmod -R 777 /srv/gitlab-swarm

```

3. Then we need to create the directory /exports/gitlab-swarm and mount srv/gitlab-swarm onto it (this is required for NFS version 4):

``` bash

mkdir -p /exports/gitlab-swarm
mount --bind /srv/gitlab-swarm /exports/gitlab-swarm

```

4. Setup the NFS share by editing /etc/exports:

``` bash

# /etc/exports

/exports/               *(rw,sync,fsid=0,crossmnt,no_subtree_check)
/exports/gitlab-swarm   *(rw,sync,no_root_squash,no_subtree_check)

```

5. Now we reload the NFS configuration: `exportfs -ra`

6. we need to add the following line to /etc/fstab: `/srv/gitlab-swarm/      /exports/gitlab-swarm/  none    bind`

7. Remember that we need the NFS client installed on each node of the cluster: `sudo apt install -y nfs-common`

8. To test if the NFS configuration is correct, we can try mounting the share:

``` bash
mkdir /var/tmp/test-nfs && \
mount -t nfs4 127.0.0.1:/gitlab-swarm /var/tmp/test-nfs && \
grep nfs4 /proc/mounts | cut -d ' ' -f 1,2,3 && \
umount /var/tmp/test-nfs

```

9. Running the commands above should output this: `127.0.0.1:/gitlab-swarm /var/tmp/test-nfs nfs4`


**Building the stack**

1. Create the configuration files for the services we are deploying. The first one is for Gitlab itself (gitlab.rb).

2. The Prometheus configuration file to setup metrics collection from gitlab

3. The Grafana configuration file

**Services**

1. Now we can start defining the services of our stack. Let's begin with Gitlab itself: stack.yml

**Deploying the stack**

1. `docker stack deploy -c stack.yaml gitlab`

2. And if you access `gitlab.localtest.me` you get to our Gitlab instance running on Docker Swarm.



## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details