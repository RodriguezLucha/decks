from pprint import pprint


def test_create_deck_successful(clear_tables, client):
    res = client.post("/decks", json={"name": "test"})
    assert res.status_code == 201
    assert res.json["name"] == "test"
    assert "id" in res.json


def test_read_single(client):
    res = client.post("/decks", json={"name": "test"})
    assert res.status_code == 201
    assert res.json["name"] == "test"
    id = res.json["id"]

    res = client.get(f"/decks/{id}")
    assert res.status_code == 200, res.json


def test_read_all(client):
    res = client.post("/decks", json={"name": "test"})
    assert res.status_code == 201
    assert res.json["name"] == "test"
    res = client.get(f"/decks")
    assert res.status_code == 200, res.json
