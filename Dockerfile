FROM python:3.11-alpine
ADD helloworld.py /

#install dependencies
RUN pip install flask
RUN pip install flask_restful

#start hello world app
EXPOSE 3333
CMD [ "python", "./helloworld.py"]docke