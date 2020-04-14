# Nginx mapping subdomain to service name - GitLab


## Requirements

- Ubuntu

## Create network

`docker network create --driver overlay proxy`

## Create some services

``` bash

docker service create --name service-1 \
    --network proxy --label traefik.port=80 nginx && \
docker service create --name service-2 \
    --network proxy --label traefik.port=80 httpd

```

## Create nginx swarm config

`docker config create nginx.conf ./nginx.conf`

## Deploy nginx service

```bash

docker service create --name nginx \
    --publish 80:80
    --network proxy
    --config source=nginx.conf,target=/etc/nginx/conf.d/default.conf
    nginx

```

## TODO

1. It is necessary [port mapping](https://github.com/livioribeiro/swarm-proxy-strategies)

2. Update stack.yml and nginx.conf (first draft)

## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details