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
    return '<h1>Hello from Index method</h2>'

@app.route('/service1')
def service1_geek():
    return '<h1>Hello from Service method - #1</h2>'

@app.route('/service2')
def service2_geek():
    return '<h1>Hello from Service method - #2</h2>'

if __name__ == '__main__':
    app.run('0.0.0.0','3333')