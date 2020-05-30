## quickstart-python

A simple Python app (using Flask) which can easily be deployed to Docker.

This application support the [Getting Started with Python](https://docs.docker.com/compose/gettingstarted/) on Docker article - check it out.

### Running locally

```
$ git clone https://github.com/mikespub-org/docker-quickstart-python.git
$ cd docker-quickstart-python
$ docker build --tag quickstart-python .
$ docker run -d -p 5080 quickstart-python
```

Alternatively, you can run the dockerized version:

```
$ docker run -d -p 5080 mikespub/quickstart-python
```

Your app should now be running:

```
curl 192.168.59.103:49153
Hello World!</br>Hostname: ebf2b5258db0</br>Counter: Redis Cache not found, counter disabled.
```

### Deploying with Docker Compose

[Install Docker Compose.](https://docs.docker.com/compose/install/)

```
$ docker-compose up 
```

### Building with Docker App

[Install Docker App.](https://github.com/docker/app#installation)

```
$ docker app init --compose-file docker-compose.yml python-app
$ ...
$ docker app inspect python-app.dockerapp
$ docker app validate python-app.dockerapp
$ docker app render python-app.dockerapp
$ docker swarm init (if necessary)
$ docker app install python-app.dockerapp --name my-app
$ docker app status my-app
$ docker app bundle python-app.dockerapp
$ docker app push --tag mikespub/python-app:0.1.0
```

### Deploying with Docker App

[Install Docker App.](https://github.com/docker/app#installation)

```
$ docker app inspect mikespub/python-app:latest
$ docker app install mikespub/python-app:latest
```

**Continue with this tutorial [here](https://docs.docker.com/compose/gettingstarted/).**
