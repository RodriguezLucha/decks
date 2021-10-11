import pytest
import time
import subprocess

from api.app import app as app_instance
from api.database import db
from api.models import Deck, Card


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    retry_run_cmd("flask db upgrade")  # Load Database Schema


@pytest.fixture(scope="session")
def app():
    app_instance.config["FLASK_DEBUG"] = False
    return app_instance


@pytest.fixture()
def db_session():
    return db.session


@pytest.fixture
def clear_table(db_session):
    db_session.query(Card).delete()
    db_session.query(Deck).delete()
    db_session.commit()


def run_cmd(cmd):
    return subprocess.check_output(
        cmd, stderr=subprocess.STDOUT, universal_newlines=True, shell=True
    )


def retry_run_cmd(cmd):

    max_tries = 10
    tries = 0

    while tries < max_tries:
        try:
            run_cmd(cmd)
            break
        except Exception:
            tries += 1
            time.sleep(1)
