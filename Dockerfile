# Use an official Python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

ARG CACHEBUST=1
# Copy your application code
COPY . /app

# UV setup and sync
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv sync --no-dev

EXPOSE 5000


# Command to run the FastAPI app
CMD ["uv", "run", "streamlit", "run", "ui/ui.py", "--server.port=5000", "--server.address=0.0.0.0"]
