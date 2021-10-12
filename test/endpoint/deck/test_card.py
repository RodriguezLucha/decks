import pytest
from pprint import pprint


def test_create_card_successful(client, existing_card_id):
    assert existing_card_id[0]
    assert existing_card_id[1]


def test_read_single(client, existing_deck_id, existing_card_id):
    res = client.get(f"/decks/{existing_card_id[0]}/cards/{existing_card_id[1]}")
    assert res.status_code == 200, res.json


def test_read_all(client, existing_card_id):
    res = client.get(f"/decks/{existing_card_id[0]}/cards")
    assert res.status_code == 200, res.json


def test_update_card(client, existing_card_id):

    res = client.patch(
        f"/decks/{existing_card_id[0]}/cards/{existing_card_id[1]}",
        json={"name": "updated_card_name"},
    )
    assert res.status_code == 200, res.json
    assert res.json["name"] == "updated_card_name"


def test_delete_card(client, existing_card_id):

    res = client.delete(f"/decks/{existing_card_id[0]}/cards/{existing_card_id[1]}")
    assert res.status_code == 200, res.json
