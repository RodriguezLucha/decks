import logging

from flask_restplus import Resource, fields, marshal
from api.serializers import card_serializers

from api.service.card_service import CardService

from api.restplus import api
from werkzeug.datastructures import FileStorage


ns = api.namespace(name="Cards", path="/decks/<int:deck_id>/cards")

log = logging.getLogger(__name__)


@ns.route("/")
@ns.route("", doc=False)  # makes '/' optional
class CardList(Resource):
    @ns.response(200, "Success", card_serializers.card_list_fields)
    def get(self, deck_id):
        card = CardService()
        result = card.get_cards(deck_id)
        return (
            marshal(
                {"data": result},
                card_serializers.card_list_fields,
            ),
            200,
        )

    post_args = api.model(
        "CardPostArgs",
        {
            "back_svg": fields.String(min_length=1, required=True),
            "front_svg": fields.String(min_length=1, required=True),
            "hidden": fields.Boolean(required=True),
            "name": fields.String(min_length=1, required=True),
            "num": fields.Integer(min_length=1, required=True),
        },
    )

    @ns.expect(post_args)
    @ns.response(201, "Created", card_serializers.card_fields_obj)
    def post(self, deck_id):
        card_service = CardService()

        result, code = card_service.create_card(deck_id, api.payload)
        if code == 201:
            return (
                marshal(
                    result,
                    card_serializers.card_fields_obj,
                ),
                code,
            )
        else:
            return result, code


@ns.route("/<int:card_id>")
@ns.param("card_id", "the card id")
class Card(Resource):
    @ns.response(200, "Success", card_serializers.card_fields_obj)
    def get(self, deck_id, card_id):

        card_service = CardService()
        card = card_service.get_card(card_id)
        if card:
            return (
                marshal(
                    card,
                    card_serializers.card_fields_obj,
                ),
                200,
            )
        else:
            return {}, 404

    @ns.response(200, "Success", card_serializers.card_fields_obj)
    def patch(self, deck_id, card_id):

        card_service = CardService()
        card = card_service.get_card_or_raise(card_id)
        result, code = card_service.update_card(card, api.payload)

        if code == 200:
            return (marshal(result, card_serializers.card_fields_obj), code)
        else:
            return result, code

    upload_parser = api.parser()
    upload_parser.add_argument(
        "file", location="files", type=FileStorage, required=True
    )

    @api.expect(upload_parser)
    def post(self, deck_id, card_id):

        args = self.upload_parser.parse_args()

        card_service = CardService()
        card = card_service.get_card_or_raise(card_id)

        result, code = card_service.upload_file(card, args["file"])

        if code == 201:
            return (marshal(result, card_serializers.card_fields_obj), code)
        else:
            return result, code

    @ns.response(200, "Success", card_serializers.card_fields_obj)
    def delete(self, deck_id, card_id):

        card_service = CardService()
        card = card_service.get_card_or_raise(card_id)
        result, code = card_service.delete_card(card)

        if code == 200:
            return (marshal(result, card_serializers.card_fields_obj), code)
        else:
            return result, code


@ns.route("/<int:card_id>/file")
@ns.param("card_id", "the card id")
class CardDownload(Resource):
    def get(self, deck_id, card_id):

        card_service = CardService()
        card = card_service.get_card_or_raise(card_id)

        result = card_service.download_file(card)
        return result
