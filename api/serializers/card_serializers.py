from flask_restplus import fields
from api.restplus import api


card_fields_obj = api.model(
    "CardObj",
    {
        "id": fields.Integer(attribute="card_id"),
        "deck_id": fields.Integer(attribute="deck_id"),
        "back_svg": fields.String(),
        "front_svg": fields.String(),
        "hidden": fields.Boolean(),
        "last_practice_date": fields.String(),
        "modified_date": fields.String(),
        "name": fields.String(example="The name of the card"),
        "num": fields.Integer(),
    },
)
card_list_fields = api.model(
    "CardList",
    {"data": fields.List(fields.Nested(card_fields_obj))},
)
