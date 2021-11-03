import os
import socket
import sys
import time

from flask import Flask, escape, json, request
from redis import Redis, RedisError
from fix_proxy import add_wsgi_proxy

# Connect to Redis
redis = Redis(host="redis", db=0)

app = Flask(__name__)
# Wrapping app.wsgi_app instead of app means that app still points at your Flask application, not at the middleware.
app.wsgi_app = add_wsgi_proxy(app.wsgi_app)


@app.route("/")
def hello():
    info = json.dumps(request.environ, indent=2, default=lambda o: repr(o))
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    tmpl = (
        "<h3>Hello {name}!</h3>"
        "<b>Hostname:</b> {hostname}<br/>"
        "<b>Visits:</b> {visits}<br/>"
        "<b>File:</b> {file}<br/>"
        "<b>Modified:</b> {date}<br/>"
        "<b>Python:</b> {version}<br/>"
        "<b>Environ:</b> <pre>{environ}</pre>"
    )
    return tmpl.format(
        name=os.getenv("APP_NAME", "World"),
        hostname=socket.gethostname(),
        visits=visits,
        file=__file__,
        date=time.ctime(os.path.getmtime(__file__)),
        version=escape(sys.version),
        environ=escape(info),
    )


if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST", "0.0.0.0"), port=int(os.getenv("FLASK_PORT", 5080))
    )
