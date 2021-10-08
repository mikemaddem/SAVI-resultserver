from os import environ

BALLOTSERVER_URL = environ.get("BALLOTSERVER_URL", "http://localhost:8000")
