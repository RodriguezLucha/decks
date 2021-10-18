from api.database import db
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    Text,
)
from sqlalchemy.orm import relationship


# sqlacodegen postgresql://postgres:password@localhost:5432/deck > output.py


class Deck(db.Model):
    __tablename__ = "deck"

    deck_id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(Text)
    modified_date = Column(DateTime)


class Card(db.Model):
    __tablename__ = "card"

    card_id = Column(
        Integer,
        primary_key=True,
    )
    back_audio = Column(LargeBinary)
    back_svg = Column(Text)
    back_text = Column(Text)
    category = Column(Text)
    deck_id = Column(ForeignKey("deck.deck_id", ondelete="RESTRICT"), nullable=False)
    front_svg = Column(Text)
    front_text = Column(Text)
    hidden = Column(Boolean, default=False)
    last_practice_date = Column(DateTime)
    modified_date = Column(DateTime)
    name = Column(Text)
    num = Column(Integer)

    deck = relationship("Deck")
