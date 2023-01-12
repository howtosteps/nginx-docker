# Create Nginx Reverse Proxy server
This has 2 steps : 
* Update the nginx configuration file `default.conf` with the desired routing of traffic
* Create a docker container that has this configuration

## Update Nginx Configuration file
Add the following lines :
```
    location /service1 {
        proxy_pass http://host.docker.internal:3333/service1;
    }

    location /service2 {
        proxy_pass http://host.docker.internal:3333/service2;
    }

    location /external {
        proxy_pass http://news.google.com;
    }
```
This tells Nginx to : 
* Forward any request from /service1 to http://host.docker.internal:3333/service1. Note that ***localhost*** entry will not work here since the web-app is running within a container on your localhost. Hence,`host.docker.internal`
* Forward any request from /service2 to http://host.docker.internal:3333/service2
* Forward any request from /external to http://news.google.com. This is just for testing purposes



## Update Nginx Dockerfile
Copy following content to `DockerFile.nginx`. Please note that we cannot use `Dockerfile` as that is already referenced by the web-app
```
# using Nginx base image
FROM nginx
# delete nginx default .conf .file
RUN rm /etc/nginx/conf.d/default.conf

# add the .conf file we have created
COPY default.conf /etc/nginx/conf.d/default.conf

#start the nginx server
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
```

This tells Docker to:

* Build an image starting with the `nginx` base image
* Remove the old configuration file
* Replace it with the newly updated `default.conf`
* Start the nginx server
