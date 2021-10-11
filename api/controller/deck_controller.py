import logging

from flask_restplus import Resource, fields, marshal
from api.serializers import deck_serializers

from api.service.deck_service import DeckService

from api.restplus import api


ns = api.namespace(name="Deck", path="/decks")

log = logging.getLogger(__name__)


@ns.route("/")
@ns.route("", doc=False)  # makes '/' optional
class DeckList(Resource):

    post_args = api.model(
        "StationCategoryPostArgs",
        {
            "name": fields.String(
                min_length=1, required=True, example="The name of the deck"
            ),
        },
    )

    @ns.expect(post_args)
    @ns.response(201, "Created", deck_serializers.deck_fields_obj)
    def post(self):
        deck_service = DeckService()

        result, code = deck_service.create_deck(api.payload)
        if code == 201:
            return (
                marshal(
                    result,
                    deck_serializers.deck_fields_obj,
                ),
                code,
            )
        else:
            return result, code


@ns.route("/<int:deck_id>")
@ns.param("deck_id", "the deck id")
class Deck(Resource):
    @ns.response(200, "Success", deck_serializers.deck_fields_obj)
    def get(self, deck_id):

        deck_service = DeckService()
        deck = deck_service.get_deck(deck_id)
        if deck:
            return (
                marshal(
                    deck,
                    deck_serializers.deck_fields_obj,
                ),
                200,
            )
        else:
            return {}, 404
