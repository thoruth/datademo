
# Requirements

This demo was made in docker to install automatically the package, and to run a temporal PostgreSQL database.


But to run the notebooks locally, install the requirements.txt

In order to run, 
Docker and docker-compose needed. Install these softwares from
https://www.docker.com/get-started

Docker engine minimum version needed: 18.02.0+


# Boot up

```bash
docker-compose up --build
```

# Stop containers

```bash
docker-compose down --volumes
```


# Jupyter

The url for notebook is http://localhost:8888
The password is `password`

# Postgres
The uri for the db is localhost:5432

authenticatio nis : `postgres:password`

# Tasks

The refactored script can be found in the notebook browser, or open locally in the workspace/interview_refactored.py

My solution explained in the solution.MD.
