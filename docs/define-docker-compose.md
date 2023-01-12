# Define Docker Compose 
Now we will define the `docker-compose.yaml` file that references both the web-app and nginx-reverse-proxy containers we just defined by using their respective Dockefile's

## Create docker-compose.yaml
Create and copy the following contents to `docker-compose.yaml`

```
version: '3'
services:
  nginx:
    build:
      context: .
      dockerfile: Dockerfile.nginx
    ports:
        - 80:80
    depends_on:
        - web
  web:
    build:
      context: .
    ports:
      - 3333:3333
```

This tells Docker Compose to :

* Define service `nginx`. This uses dockerfile:`Dockerfile.nginx` and runs on port 80
* For simplicity, we have mapped the internal container port to the external container port
* Define service `web`. This uses default `Dockerfile` and runs on port 3333
