# Use an official Python 3.10 image from Docker Hub
# to build locally - docker build --no-cache  -t  test .
# run locally - docker run --rm -d -p 5000:5000 test
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy your application code
COPY . /app

# UV setup and sync
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync --no-dev

EXPOSE 5000


# Command to run the FastAPI app
# CMD ["uv", "run", "streamlit", "run", "app.py"]
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=5000", "--server.address=0.0.0.0"]
