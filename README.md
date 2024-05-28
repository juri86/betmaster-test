# Test Project

### Install

* Install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) package manager
* [Docker](https://docs.docker.com/desktop/install/mac-install/) has to be installed in your system.
* Install Python 3.12.3 or higher. You can download from [here](https://www.python.org/downloads/).
  Alternatively, you can use [pyenv](https://github.com/pyenv/pyenv) manager.
* Create poetry virtual environment.
    ```bash
    poetry config virtualenvs.in-project true
    ```
* Use your Python version
    ```bash
    poetry env use 3.12.3
    ```
* Install requirements from poetry.lock file
    ```bash
    poetry lock --no-update
    ```
    ```bash
    poetry install
    ```

### Local Run
* start docker env
    ```bash
    docker compose -f ./docker/docker-compose.yml up -d
    ```
* execute tests inside docker container
    ```bash
  
    docker exec -it automation sh -c "cd ./betmaster-test; python -m pytest tests/prod -v"
    ```
* stop docker env
    ```bash
    docker compose -f ./docker/docker-compose.yml down
    ```
  
