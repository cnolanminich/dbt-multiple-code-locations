# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /opt/dagster/app

COPY . /opt/dagster/app

# Add steps to install the Python dependencies for your Dagster project
# into the default Python on PATH
# For example, this project uses setup.py and we install all dependencies into the Docker container
# using `pip`. 

RUN uv pip install --system -e .