import logging
from api.database import db
from api.models import Deck

log = logging.getLogger(__name__)


class DeckService:
    def create_deck(self, body):
        deck = Deck()
        for key, value in body.items():
            setattr(deck, key, value)

        try:
            db.session.add(deck)
            db.session.commit()
        except Exception:
            db.session.rollback()

        return deck, 201

    def get_deck(self, deck_id):

        station_category = db.session.query(Deck).filter_by(deck_id=deck_id).first()
        return station_category

    def get_deck_or_raise(self, deck_id):
        deck = self.get_deck(deck_id)
        if not deck:
            raise ("Deck not found!")

        return deck

    def update_deck(self, deck, body):

        for key, value in body.items():
            setattr(deck, key, value)

        try:
            db.session.add(deck)
            db.session.commit()
        except Exception:
            db.session.rollback()

        return deck, 200

    def get_decks(self):

        station_category = db.session.query(Deck).all()
        return station_category

    def delete_deck(self, deck):
        try:
            db.session.delete(deck)
            db.session.commit()
        except Exception:
            db.session.rollback()
        return deck, 200
