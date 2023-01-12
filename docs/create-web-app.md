
# Create Web App

Create a simple web-app that uses python flask API and exposes 3 services :

* http://localhost:3333/ - returns msg : `<h2>Hello from Index method</h2>` 
* http://localhost:3333/service1 - returns msg : `<h2>Hello from Service method - #1</h2>`
* http://localhost:3333/service2 - returns msg : `<h2>Hello from Service method - #2</h2>`

## Create starter python file
Create file `helloworld.py` and copy the following content in there : 

```
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#class Greeting (Resource):
#    def get(self):
#        return 'Hello World!'
#api.add_resource(Greeting, '/') # Route_1

@app.route('/')
def index_geek():
    return '<h2>Hello from Index method</h2>'

@app.route('/service1')
def service1_geek():
    return '<h2>Hello from Service method - #1</h2>'

@app.route('/service2')
def service2_geek():
    return '<h2>Hello from Service method - #2</h2>'

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
```
## Create Dockerfile
Now we will create the docker file for the web app. Create a file `Dockerfile` and copy the following : 

```
FROM python:3.11-alpine
ADD helloworld.py /

#install dependencies
RUN pip install flask
RUN pip install flask_restful

#start hello world app
EXPOSE 3333
CMD [ "python", "./helloworld.py"]
```

This tells Docker to:

* Build an image starting with the `python 3.11-alpine` base image
* Install the Python dependencies - flask & flask_restful
* Expose port 3333
* Set the default command for the container to run on start-up
