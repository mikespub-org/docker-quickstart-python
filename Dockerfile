# Using official python runtime base image
FROM python:3.9.4-slim

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD *.py /app/

# Make port 5080 available for links and/or publish
ENV FLASK_PORT 5080
EXPOSE $FLASK_PORT

# Environment Variables
ENV FLASK_HOST 0.0.0.0
ENV NAME World

# Define our command to be run when launching the container
CMD ["gunicorn", "-c", "guniconfig.py", "app:app"]
