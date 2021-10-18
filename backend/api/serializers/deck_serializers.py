from flask_restplus import fields
from api.restplus import api


deck_fields_obj = api.model(
    "DeckObj",
    {
        "id": fields.Integer(attribute="deck_id"),
        "name": fields.String(example="The name of the deck"),
    },
)
deck_list_fields = api.model(
    "DeckList",
    {"data": fields.List(fields.Nested(deck_fields_obj))},
)
