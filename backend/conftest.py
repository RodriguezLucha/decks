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
def clear_tables(db_session):
    db_session.query(Card).delete()
    db_session.query(Deck).delete()
    db_session.commit()


@pytest.fixture
def existing_deck_id(client):
    res = client.post(
        "/decks",
        json={"name": "name"},
    )
    assert res.status_code == 201
    deck_id = res.json["id"]
    yield deck_id


@pytest.fixture
def existing_card_id(client, existing_deck_id):
    res = client.post(
        f"/decks/{existing_deck_id}/cards",
        json={
            "name": "name",
            "num": 1,
            "front_svg": "front",
            "back_svg": "back",
            "front_text": "front",
            "back_text": "back",
            "category": "category",
            "hidden": False,
        },
    )
    assert res.status_code == 201, res.json
    card_id = res.json["id"]
    yield existing_deck_id, card_id


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
