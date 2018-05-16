# Demo for my Docker talk on [TechEd 2018](https://teched.cz)

    Ondrej Sika <ondrej@ondrejsika.com>

See slides here: <https://ondrej-sika.cz/blog/2018/teched>


## Run with Docker command

```
docker build -t teched18 .
docker run --name redis -d redis:alpine
docker run --link redis -p 80:80 teched18
```


## Run with Docker Compose

```
docker-compose up
```


## Run with Docker Swarm

```
docker-compose build
docker-compose push
docker stack deploy --compose-file docker-compose.yml teched18
```

