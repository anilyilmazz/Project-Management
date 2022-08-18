# Project Management App
Project management app is a work control system. Users can create their project, works and make comments to works.

Project Management App Tech Stack:
- [Python] - Python is a high-level, interpreted, general-purpose programming language
- [Flask] - Flask is a micro web framework written in Python
- [Docker] - Docker is an open platform for developing, shipping, and running applications
- [MongoDB] - Document based NoSQL database
- [MongoEngine] - MongoEngine is an Object-Document Mapper, written in Python for working with MongoDB
- [Celery] - Celery is an open source asynchronous task queue or job queue which is based on distributed message passing
- [Redis] - The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker

## Installation
**Requires docker and docker engine

Build project with docker compose and run:
```sh
docker compose build
docker compose up
```

Access project at http://127.0.0.1:5000/ address

## API Swagger

Swagger url is "/doc" at project.

![alt text](https://i.ibb.co/QP5tv5t/Screenshot-27.png)

## Features

- Get project, works and comments
- Manage project, works and comments
- Manage work planned start and finish dates with email


   [Python]: <https://www.python.org/>
   [Flask]: <https://flask.palletsprojects.com/en/2.2.x/>
   [MongoDB]: <https://www.mongodb.com/>
   [Docker]: <https://www.docker.com/>
   [MongoEngine]: <https://docs.mongoengine.org/>
   [Redis]: <https://redis.io/>
   [Celery]: <https://docs.celeryq.dev/>
   
