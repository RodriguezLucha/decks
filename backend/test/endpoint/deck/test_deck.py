def test_create_deck_successful(existing_deck_id):
    assert existing_deck_id


def test_read_single(client, existing_deck_id):
    res = client.get(f"/decks/{existing_deck_id}")
    assert res.status_code == 200, res.json


def test_read_all(client, existing_deck_id):
    res = client.get("/decks")
    assert res.status_code == 200, res.json


def test_update_deck(client, existing_deck_id):

    res = client.patch(f"/decks/{existing_deck_id}", json={"name": "updated_name"})
    assert res.status_code == 200, res.json
    assert res.json["name"] == "updated_name"


def test_delete_deck(client, existing_deck_id):

    res = client.delete(f"/decks/{existing_deck_id}")
    assert res.status_code == 200, res.json
