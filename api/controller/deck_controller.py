import logging
from pprint import pprint

from flask_restplus import Resource, fields, marshal
from api.serializers import deck_serializers

from api.service.deck_service import DeckService

from api.restplus import api


ns = api.namespace(name="Deck", path="/decks")

log = logging.getLogger(__name__)


@ns.route("/")
@ns.route("", doc=False)  # makes '/' optional
class DeckList(Resource):
    @ns.response(200, "Success", deck_serializers.deck_list_fields)
    def get(self):
        deck = DeckService()
        result = deck.get_decks()
        return (
            marshal(
                {"data": result},
                deck_serializers.deck_list_fields,
            ),
            200,
        )

    post_args = api.model(
        "DeckPostArgs",
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

    @ns.response(200, "Success", deck_serializers.deck_fields_obj)
    def patch(self, deck_id):

        """
        Edit a single Station Category
        """
        deck_service = DeckService()
        deck = deck_service.get_deck_or_raise(deck_id)
        result, code = deck_service.update_deck(deck, api.payload)

        if code == 200:
            return (marshal(result, deck_serializers.deck_fields_obj), code)
        else:
            return result, code
