# Using official python runtime base image
FROM python:3.12-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED=True

# Set the application directory
ENV APP_HOME=/app
WORKDIR $APP_HOME

# See https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install our requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
COPY *.py /app/

# Make port 5080 available for links and/or publish
ENV FLASK_PORT=5080
EXPOSE $FLASK_PORT

# Environment Variables
ENV FLASK_HOST=0.0.0.0
ENV APP_NAME=Docker
ENV PROXY_FIX=0
ENV PROXY_FIX_FOR=1 PROXY_FIX_PROTO=1 PROXY_FIX_HOST=0 PROXY_FIX_PORT=0 PROXY_FIX_PREFIX=0

# Define our command to be run when launching the container
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
