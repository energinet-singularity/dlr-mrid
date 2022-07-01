# Select base-image
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=0

# Install pip requirements
COPY app/requirements.txt /
RUN apt-get update && apt install -y git 
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir && rm requirements.txt


COPY app/* /app/
COPY tests/valid-testdata/* /test_data/

EXPOSE 5000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3","-u", "/app/main.py"]
