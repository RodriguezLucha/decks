import logging
from api.database import db
from api.models import Card
from flask import send_file
import io

log = logging.getLogger(__name__)


class CardService:
    def create_card(self, deck_id, body):
        card = Card()
        card.deck_id = deck_id
        for key, value in body.items():
            setattr(card, key, value)

        try:
            db.session.add(card)
            db.session.commit()
        except Exception:
            db.session.rollback()

        return card, 201

    def get_card(self, card_id):

        station_category = db.session.query(Card).filter_by(card_id=card_id).first()
        return station_category

    def get_card_or_raise(self, card_id):
        card = self.get_card(card_id)
        if not card:
            raise ("Card not found!")

        return card

    def update_card(self, card, body):

        log.info(card)
        log.info(body)

        for key, value in body.items():
            setattr(card, key, value)

        try:
            db.session.add(card)
            db.session.commit()
        except Exception:
            db.session.rollback()

        return card, 200

    def upload_file(self, card, file):

        card.back_audio = file.stream.read()

        try:
            db.session.add(card)
            db.session.commit()
        except Exception:
            db.session.rollback()

        return card, 201

    def download_file(self, card):

        memory = io.BytesIO()
        memory.write(card.back_audio)
        memory.seek(0)
        return send_file(
            memory,
            # mimetype=guessed_mimetype,
            # as_attachment=True,
            attachment_filename="audio.mp3",
        )

    def get_cards(self, deck_id):

        cards = db.session.query(Card).filter_by(deck_id=deck_id).all()
        return cards

    def delete_card(self, card):
        try:
            db.session.delete(card)
            db.session.commit()
        except Exception:
            db.session.rollback()
        return card, 200
