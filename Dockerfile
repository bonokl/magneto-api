# Use a minimal Python 3.12 base image for building dependencies
FROM python:3.12-slim AS builder

# Prevent Python from writing .pyc files to disk (saves space, keeps things clean)
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory in the container
WORKDIR /app

# Install build tools and PostgreSQL dev libraries (needed for compiling psycopg2)
RUN apt-get update && \
    apt-get install -y \
    git \
    build-essential \
    libpq-dev && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment inside the image
RUN python -m venv /venv

# Copy the requirements file and install Python dependencies into the virtualenv
COPY requirements.txt requirements.txt
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Start from a clean slim image for runtime, keeping the final image small
FROM python:3.12-slim

# Ensure Python output is unbuffered for real-time logging in Docker
ENV PYTHONUNBUFFERED=1

# Set working directory in the runtime container
WORKDIR /app

# Install only runtime dependency: the libpq shared library required by psycopg2
RUN apt-get update && \
    apt-get install -y libpq5 && \
    rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from the builder stage
COPY --from=builder /venv /venv

# Copy the application code into the container
COPY . .

# Add virtualenv's bin directory to the PATH so its Python and tools are used
ENV PATH="/venv/bin:$PATH"

# Launch the app with Gunicorn and Uvicorn workers, binding to a specific port
ENTRYPOINT ["gunicorn", "-w", "5", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "src.main.main:app"]
