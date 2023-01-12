# Copy Nginx Configuration file 
The first step is to get a sample nginx configuation file `default.conf` from a base image. For this project, we will use Docker Hub's latest image:`nginx'.

Create & go to your project folder `nginx-docker` 
```
PS C:\Users\aniru> cd ~\workspace\github\nginx-docker
```

## Start the nginx container
Now start the nginx container from the base image from Docker Hub
```
docker run -d --name nginx-base -p 80:80 nginx
```

## Copy the nginx conf file
Here we copy the nginx configuration file to your local folder 
```
docker cp nginx-base:/etc/nginx/conf.d/default.conf .
```

## Stop the nginx container
We don't need the nginx container anymore. So let's stop the container. 
```
PS C:\Users\aniru\workspace\github\nginx-docker> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                NAMES      
0e1687e6cd57   nginx     "/docker-entrypoint.…"   53 minutes ago   Up 53 minutes   0.0.0.0:80->80/tcp   nginx      
PS C:\Users\aniru\workspace\github\nginx-docker> docker stop nginx
nginx
```