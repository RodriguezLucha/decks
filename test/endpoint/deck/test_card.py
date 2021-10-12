from filehash import FileHash
import os
import io


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


def test_upload_a_file(clear_tables, client, existing_card_id):
    content = None
    with open("cactus.jpg", "rb") as fin:
        content = io.BytesIO(fin.read())

    data = dict(file=(content, "cactus.jpg"))

    res = client.post(
        f"/decks/{existing_card_id[0]}/cards/{existing_card_id[1]}",
        content_type="multipart/form-data",
        data=data,
    )
    assert res.status_code == 201, res.json

    res = client.get(
        f"/decks/{existing_card_id[0]}/cards/{existing_card_id[1]}/file",
    )

    assert res.status_code == 200, res.json

    downloaded_filename = "download.jpg"

    f = open(downloaded_filename, "wb")
    f.write(res.data)
    f.close()

    sha1hasher = FileHash("sha1")
    downloaded_hash = sha1hasher.hash_file(downloaded_filename)
    assert downloaded_hash == "1dbce80ad580d7fb7def9db03bd430c2d04c9bf6"
    os.remove(downloaded_filename)
