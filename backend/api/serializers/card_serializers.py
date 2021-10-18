from flask_restplus import fields
from api.restplus import api


card_fields_obj = api.model(
    "CardObj",
    {
        "back_svg": fields.String(),
        "back_text": fields.String(),
        "category": fields.String(),
        "deck_id": fields.Integer(attribute="deck_id"),
        "front_svg": fields.String(),
        "front_text": fields.String(),
        "hidden": fields.Boolean(),
        "id": fields.Integer(attribute="card_id"),
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
