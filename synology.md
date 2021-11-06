### Deploy with Portainer on Synology NAS (known bug)

Deploying individual Docker containers is easy on Synology NAS, either via the Docker package web interface or via the *docker* CLI.

Deploying complete *docker-compose* templates via CLI is also feasible, but for anything more you would typically switch to using something like [Portainer](https://docs.portainer.io/v/ce-2.9/user/home) to manage your Docker stacks, services, containers, volumes, networks, images etc.

Unfortunately, using *docker stack* via CLI or Portainer App templates presents a bit of a challenge on Synology NAS devices. Due to a *known bug* of Docker on Synology, environment parameters defined for services are **not** passed along to create the actual containers.

This makes using Portainer to deploy a complete stack or re-configure your services via environment variables difficult compared to other platforms...

Here are some possible work-arounds you can use:

a. Update the stack template with the right template values whenever you want to (re-)deploy

```
version: '3.6'
services:
  web:
	#...
    ports:
      - "5080:5080"
    environment:
      HOST_PORT: 5080
      FLASK_PORT: 5080
      FLASK_HOST: "0.0.0.0"
      APP_NAME: "Template"
	  #...
```

b. Use docker configs in your template to pass along a .env file, and override the image CMD if needed

```
version: '3.6'
services:
  web:
	#...
    #env_file: /data/container_env/env.quickstart-python
    command: sh -c '. .env && gunicorn -c gunicorn.conf.py app:app'
    configs:
      - source: env_config
        target: /app/.env
        mode: 0755
configs:
  env_config:
    # path from portainer perspective, where /data is a bind mount from /volume1/docker/portainer on the host
    file: /data/container_env/env.quickstart-python
```

with /data/container-env a folder you create on the portainer /data volume (or the corresponding host directory) *once* to hold the environment variables for all deployments. One draw-back here is that whenever the configuration changes, you need to change the name of the config as well.

c. Use docker volumes in your template to mount an env/ folder, and override the image CMD if needed

```
version: '3.6'
services:
  web:
	#...
    #env_file: /data/container_env/env.quickstart-python
    volumes:
      - portainer-env:/app/env
    command: sh -c '. /app/env/env.quickstart-python && gunicorn -c gunicorn.conf.py app:app'
volumes:
  portainer-env:
    external: true
```

with portainer-env a docker volume you create *once* to hold the environment variables for all deployments, e.g. as a bind mount of some directory on the host, or as a separate docker volume.

```
version: '3.6'
volumes:
  portainer-env:
    driver: local
    driver_opts:
       o: bind
       type: none
       device: /volume1/docker/portainer/container_env
```

