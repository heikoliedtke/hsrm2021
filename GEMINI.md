# GEMINI Project Analysis: hsrm2021

## Project Overview

This project, `hsrm2021`, appears to be a collection of examples for a university course, likely related to web technologies and containerization. The repository contains several distinct components, primarily focused on demonstrating web server setup and simple web applications using Docker, Nginx, and Python/Flask.

The project is structured into three main directories: `container01`, `container02`, and `container03`, each intended to be a self-contained unit. A GitHub Actions workflow is in place to automatically build Docker images for the first two containers.

## Key Technologies

*   **Containerization**: Docker
*   **Web Servers**: Nginx, uWSGI
*   **Backend**: Python 3 with Flask
*   **CI/CD**: GitHub Actions

## Component Breakdown

### `container01` - Static Nginx Server

*   **Purpose**: To demonstrate a basic, containerized web server serving a single static HTML page.
*   **Architecture**:
    *   `Dockerfile`: Uses an `ubuntu:18.04` base image, installs `nginx`, and copies the local `hsrm.html` to serve as the index page.
    *   `hsrm.html`: A static HTML file.

### `container02` - Flask Web Application

*   **Purpose**: To demonstrate a simple Python web application served in a production-style setup.
*   **Architecture**:
    *   `Dockerfile`: Sets up an `ubuntu:18.04` environment with `python3`, `nginx`, and `uwsgi`.
    *   `app.py`: A minimal Flask application with one route (`/`). It renders a template displaying basic system information (`os.uname()`).
    *   `requirements.txt`: Specifies `flask` and `uwsgi` as dependencies.
    *   `app.ini`: uWSGI configuration file that defines how to run the Flask app.
    *   `myproject`: Nginx site configuration that acts as a reverse proxy, passing requests to the uWSGI socket.
    *   `templates/base.html`: The HTML template for the Flask application.

### `container03` - Placeholder

*   **Purpose**: This component appears to be a placeholder or is incomplete.
*   **Contents**: Contains a single, empty `app.py` file. There is no associated `Dockerfile` or build configuration.

## Building and Running

The CI/CD pipeline in `.github/workflows/main.yml` provides the canonical build commands.

### Building the Containers

To build the Docker images locally, use the following commands from the project root:

```bash
# Build the static nginx container
docker build ./container01 -t hsrm/container01

# Build the Flask application container
docker build ./container02 -t hsrm/container02
```

### Running the Containers

To run the containers, you can use the following commands.

*   **Run `container01`:**
    ```bash
    # This will serve the static hsrm.html page on http://localhost:8080
    docker run -d -p 8080:80 hsrm/container01
    ```

*   **Run `container02`:**
    ```bash
    # This will serve the Flask demo app on http://localhost:8081
    docker run -d -p 8081:80 hsrm/container02
    ```

## Development Conventions

*   The project relies on a multi-container architecture.
*   The GitHub Actions workflow automates the building and pushing of container images to the GitHub Container Registry (`ghcr.io`).
*   Python dependencies are managed via `requirements.txt`.
*   There are no explicit linting or formatting rules apparent in the repository.
