FROM python:3.8

# set work directory
COPY ./jangoMiniShop /srv/www/jangoMiniShop
WORKDIR /srv/www/jangoMiniShop

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt