DROP table if exists deck cascade;

DROP table if exists card cascade;

CREATE TABLE deck (
    deck_id serial primary key,
    name text,
    modified_date timestamp
);

CREATE TABLE card (
    card_id serial primary key,
    deck_id integer,
    num integer,
    name text,
    front_svg text,
    back_svg text,
    back_audio bytea,
    hidden boolean,
    modified_date timestamp,
    last_practice_date timestamp,
    CONSTRAINT fk_deck FOREIGN KEY(deck_id) REFERENCES deck(deck_id) ON DELETE restrict
);