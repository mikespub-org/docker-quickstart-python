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

### Building with Docker App (deprecated - see Porter below)

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

### Deploying with Docker App (deprecated - see Porter below)

[Install Docker App.](https://github.com/docker/app#installation)

```
$ docker app inspect mikespub/python-app:latest
$ docker app install mikespub/python-app:latest
```

**Continue with this tutorial [here](https://docs.docker.com/compose/gettingstarted/).**

### Migrate from Docker App to Porter

https://porter.sh/blog/migrate-from-docker-app/

```
$ porter install --allow-docker-host-access
$ ...
$ porter build
$ porter publish
$ ...
$ porter explain --reference mikespub/python-app:v0.3.0
$ porter inspect --reference mikespub/python-app:v0.3.0
$ ...
$ porter install python-app --reference mikespub/python-app:v0.3.0 --allow-docker-host-access
$ porter upgrade python-app --reference mikespub/python-app:v0.3.1 --allow-docker-host-access
$ porter uninstall python-app --allow-docker-host-access
```

See https://github.com/getporter/docker-compose-mixin/tree/main/examples
and https://github.com/getporter/porter/tree/main/examples/dockerapp

### Deploy with Portainer on Synology NAS

See known bug and work-arounds at [Portainer on Synology NAS](synology.md)

### Deploy with Helm chart on Kubernetes or OpenShift

See Helm chart repository at [Mike's Pub Helm Charts](https://github-org.mikespub.net/sclorg-django-ex/) or find on [ArtifactHUB](https://artifacthub.io/packages/search?repo=mikespub-helmcharts)

```
$ helm repo add mikespub-charts https://github-org.mikespub.net/sclorg-django-ex/
$ helm install my-quickstart-python mikespub-charts/quickstart-python
```

### Create/update Helm chart for Kubernetes or templates for OpenShift

[Install Kompose.](https://github.com/kubernetes/kompose)

```
$ kompose convert -c -o quickstart-python
$ helm package quickstart-python/
$ helm install my-quickstart-python quickstart-python
```

```
$ mkdir -p openshift/templates
$ kompose convert -o openshift/templates --provider=openshift --build build-config
```

### Building with Cloud Native Buildpacks

See [Turn Your Code into Docker Images with Cloud Native Buildpacks](https://blog.heroku.com/docker-images-with-buildpacks) and [An App’s Brief Journey from Source to Image](https://buildpacks.io/docs/app-journey/)

[Install Pack.](https://buildpacks.io/docs/tools/pack/)

Create [project.toml](project.toml) to exclude/include files for the image, specify buildpacks etc.

Create [Procfile](Procfile) if you want to use heroku buildpacks:

```
$ cat Procfile
web: gunicorn app:app
```

Build (and optionally publish) container image with appropriate builder:

```
$ pack build --builder heroku/buildpacks mikespub/buildpacks-python
latest: Pulling from heroku/buildpacks
...
===> ANALYZING
[analyzer] Restoring data for SBOM from previous image
===> DETECTING
[detector] heroku/python 0.0.0
===> RESTORING
[restorer] Restoring metadata for "heroku/python:shim" from cache
[restorer] Restoring data for "heroku/python:shim" from cache
===> BUILDING
[builder] -----> No Python version was specified. Using the same version as the last build: python-3.10.8
[builder]        To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
...
[builder] -----> Installing requirements with pip
===> EXPORTING
...
[exporter] Setting default process type 'web'
[exporter] Saving mikespub/buildpacks-python...
[exporter] *** Images (sha256:7b74d89e524730f704b5e8ef56ac1ee0bcad3475be82dea885d826c5bda20bde):
[exporter]       mikespub/buildpacks-python
[exporter] Adding cache layer 'heroku/python:shim'
Successfully built image mikespub/buildpacks-python
```

Test the containerized app image with Docker:

```
$ docker run --rm -p 5080:5080 mikespub/buildpacks-python
[2022-11-21 15:37:49 +0000] [1] [INFO] Starting gunicorn 20.1.0
[2022-11-21 15:37:49 +0000] [1] [INFO] Listening at: http://0.0.0.0:5080 (1)
...
```

