import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.getenv("DOT_ENV_PATH"))

FLASK_DEBUG = True

SERVICE_NAME = "deck"
