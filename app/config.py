from decouple import RepositoryEnv, Config
import os

docker = os.environ.get("DOCKER_CONTAINER")

env_file = ".env"

if docker:
    env_file = "docker-compose.env"
    
config = Config(RepositoryEnv(env_file))

# PARAMETRS FOR DB
DB_HOST = config.get("POSTGRESQL_HOST")
DB_USER = config.get("POSTGRESQL_USER")
DB_PASSWORD = config.get("POSTGRESQL_PASSWORD")
DB_NAME = config.get("POSTGRESQL_DATABASE")
DB_PORT = config.get("POSTGRESQL_PORT")