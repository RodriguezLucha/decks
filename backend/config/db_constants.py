import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.getenv("DOT_ENV_PATH"))

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PORT = os.getenv("PORT", 5432)
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB = os.getenv("DB", "deck")

# append public to fix gen_random_uuid() not found from hasura events
DB_SCHEMA = "public"

DB_CONFIG = {"host": DB_HOST, "user": DB_USER, "passwd": DB_PASSWORD, "db": DB}
DB_CHARSET = os.getenv("CHARSET", "utf-8")
DB_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}?options=-c search_path={}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB, DB_SCHEMA
)
DB_ID = os.getenv("DB_ID") or 1

DECK_BIND_NAME = "deck"
DB_CLIENT_NAME = "deck"

# SQLAlchemy settings https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}?application_name={}&options=-c search_path={}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB, DB_CLIENT_NAME, DB_SCHEMA
)
SQLALCHEMY_BINDS = {
    DECK_BIND_NAME: DB_URI,
}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Output all generated SQL from ORM to log
SQLALCHEMY_ECHO = False
