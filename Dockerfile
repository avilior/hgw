FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL maintainer="Avi Lior <avi@lior.org>"

#create a place for our configuration file
RUN mkdir -p /etc/hgw/

#COPY ./app /app/app
COPY ./app /app