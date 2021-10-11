from flask_restplus import fields
from api.restplus import api


deck_fields_obj = api.model(
    "DeckObj",
    {
        "id": fields.Integer(attribute="deck_id"),
        "name": fields.String(example="The name of the deck"),
    },
)