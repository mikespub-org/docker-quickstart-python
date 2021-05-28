# gunicorn configuration file
import os

bind = "%s:%s" % (os.getenv("FLASK_HOST", "0.0.0.0"), os.getenv("FLASK_PORT", 5080))

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# workers = 1
# threads = 8
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
# timeout = 0
