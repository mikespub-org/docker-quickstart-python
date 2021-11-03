# gunicorn configuration file
import os

bind = "{}:{}".format(os.getenv("FLASK_HOST", "0.0.0.0"), os.getenv("FLASK_PORT", 5080))

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Using recommendations from https://pythonspeed.com/articles/gunicorn-in-docker/
workers = 2
threads = 4
worker_class = "gthread"
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
timeout = 0
# Fix heartbeat system writing to /tmp - https://docs.gunicorn.org/en/stable/faq.html#blocking-os-fchmod
worker_tmp_dir = "/dev/shm"
