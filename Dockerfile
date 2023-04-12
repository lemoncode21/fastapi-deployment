FROM python:3.9

# create app directory
WORKDIR /usr/src/app

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITTERBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .