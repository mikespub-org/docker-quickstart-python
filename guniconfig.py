# gunicorn configuration file
import os

bind = "%s:%s" % (os.getenv("FLASK_HOST", "0.0.0.0"), os.getenv("FLASK_PORT", 5080))
