from flask import Flask, escape
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0)

app = Flask(__name__)


@app.route("/")
def hello():
    from flask import request
    import json

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
        "<b>Environ:</b> <pre>{environ}</pre>"
    )
    return tmpl.format(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        visits=visits,
        file=__file__,
        environ=escape(info),
    )


if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST", "0.0.0.0"), port=int(os.getenv("FLASK_PORT", 5080))
    )
