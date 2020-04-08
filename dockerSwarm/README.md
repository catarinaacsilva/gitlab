# GitLab - Docker Swarm

- PostGresql
- Redis
- Sidekiq
- NGINX
- Prometheus
- GitLab Runner
- Unicorn Workers
- GitLab Workhorse
- Gitaly


## Requirements

- Docker

## Docker swarm - deploy

**Before we begin**

- Proxy to forward the requests to the correct services

- Postgres and Redis

- Prometheus to collect metrics from Gitlab and Grafana to visualize these metrics

- An NFS4 share to store any persistent data we need

### The proxy

- nginx TODO

###  Setting up NFS

1. `apt-get install -y nfs-kernel-server`

2. For the NFS share the will need a directory structure like the following:

```console
.
+-- /srv/gitlab-swarm
|   +-- gitlab
|       +-- config
|       +-- data
|       +-- logs
|   +-- grafana
|   +-- postgres
|   +-- prometheus
```

We can create it using the following shell:

```
mkdir -p /srv/gitlab-swarm && \
mkdir -p /srv/gitlab-swarm/gitlab/{data,logs,config} && \
mkdir -p /srv/gitlab-swarm/postgres && \
mkdir -p /srv/gitlab-swarm/grafana && \
mkdir -p /srv/gitlab-swarm/prometheus && \
chmod -R 777 /srv/gitlab-swarm
```

3. Then we need to create the directory `/exports/gitlab-swarm` and mount `srv/gitlab-swarm` onto it (this is required for NFS version 4):

```
mkdir -p /exports/gitlab-swarm
mount --bind /srv/gitlab-swarm /exports/gitlab-sw

```

4. Setup the NFS share by editing `/etc/exports`:

```
# /etc/exports

/exports/               *(rw,sync,fsid=0,crossmnt,no_subtree_check)
/exports/gitlab-swarm   *(rw,sync,no_root_squash,no_subtree_check)

```

5. Now we reload the NFS configuration: `exportfs -ra`

6. In order to make the nfs mounts persist after reboots, we need to add the following line to `/etc/fstab`: `/srv/gitlab-swarm/      /exports/gitlab-swarm/  none    bind`


7. Remember that we need the NFS client installed on each node of the cluster: `apt-get install -y nfs-common`

8. To test if the NFS configuration is correct, we can try mounting the share:

```
mkdir /var/tmp/test-nfs && \
mount -t nfs4 127.0.0.1:/gitlab-swarm /var/tmp/test-nfs && \
grep nfs4 /proc/mounts | cut -d ' ' -f 1,2,3 && \
umount /var/tmp/test-nfs

```

9. The output should be: `127.0.0.1:/gitlab-swarm /var/tmp/test-nfs nfs4`


### Building the stack

1. Write the file gitlab.rb

2. Write Prometheus configuration on prometheus.yaml

3. Write the Grafana configuration file: 

```
[database]
path = "/data/grafana.db"

[session]
provider = "redis"
provider_config = "addr=redis:6379,prefix=grafana:"


```

### Services

1. Define the services of our stack

### Deploying the stack

1. To deploy our stack, we use the docker command line: `docker stack deploy -c stack.yaml gitlab`


## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details