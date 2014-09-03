FROM debian:wheezy
MAINTAINER Paddy Carey <paddy@wackwack.co.uk>

# no tty
ENV DEBIAN_FRONTEND noninteractive

# get up to date
RUN apt-get update -y
RUN apt-get upgrade -y

# install packages from apt/PyPI
RUN apt-get install -y python-pip python-dev
RUN pip install fabric

# copy the application data into the container
ADD ./ /app/
RUN chmod 0600 /app/secrets/deploy.pem

# default run command
CMD bash
