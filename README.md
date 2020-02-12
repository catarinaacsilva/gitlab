# Deploy GitLab in a Docker swarm

You can easily configure and deploy your Docker-based GitLab installation in a swarm cluster.

In this project was used:

- GitLab
- PostgreSQL
- Redis

**GitLab**
It provides a Git-repository manager. So, It offers free unlimited (private) repositories and unlimited collaborators. 

**PostgreSQL**
It  is a free and open-source relational database management system (RDBMS) emphasizing extensibility and technical standards compliance.

**Redis**
Redis is an open-source, networked, in-memory, key-value data store with optional durability. It works like a cache.


## Requirements

- Docker

- [Docker compose](https://docs.docker.com/compose/install/)


## Install GitLab using docker-compose

1. Create a Docker-compose.yml

2. Run `docker-compose up`

**Potencial problems:** ACLs


## Setup a Docker swarm

[Docker swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/)
[docker swarm](https://docs.gitlab.com/omnibus/docker/#run-the-image)



## Extra information

[Docker-compose and Docker swarm](https://docs.gitlab.com/omnibus/docker/#run-the-image)

[GitLab Docker images](https://docs.gitlab.com/omnibus/docker/#run-the-image)

[Run Gitlab Runner in a container](https://docs.gitlab.com/runner/install/docker.html#docker-images)

[PostgresSQL DB and Omnibus GitLab](https://docs.gitlab.com/omnibus/settings/database.html)

[NFS](https://docs.gitlab.com/ee/administration/high_availability/nfs.html)

[Configuring GitLab for Scaling and High Availability](https://docs.gitlab.com/ee/administration/high_availability/gitlab.html)

[Installing trusted SSL server certificates](https://docs.gitlab.com/runner/install/docker.html#docker-images)

## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details