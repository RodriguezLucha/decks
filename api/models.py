from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.schema import UniqueConstraint
from api.database import db
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    Text,
    text,
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
    deck_id = Column(ForeignKey("deck.deck_id", ondelete="RESTRICT"))
    num = Column(Integer)
    name = Column(Text)
    front_svg = Column(Text)
    back_svg = Column(Text)
    back_audio = Column(LargeBinary)
    hidden = Column(Boolean)
    modified_date = Column(DateTime)
    last_practice_date = Column(DateTime)

    deck = relationship("Deck")
