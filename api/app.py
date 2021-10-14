import logging
from flask import Flask, Blueprint
from config import db_constants, constants
from flask_cors import CORS, cross_origin
from api.database import db, migrate

import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
from api.restplus import api  # noqa: E402

from api.controller import deck_controller, card_controller  # noqa: E402

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)
log.info("Start.")

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db_constants.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_BINDS"] = db_constants.SQLALCHEMY_BINDS
app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = db_constants.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SQLALCHEMY_ECHO"] = db_constants.SQLALCHEMY_ECHO
app.config["CORS_HEADERS"] = "Content-Type"

blueprint = Blueprint(
    constants.SERVICE_NAME,
    __name__,
)
api.init_app(blueprint)


api.add_namespace(deck_controller.ns)
api.add_namespace(card_controller.ns)
app.register_blueprint(blueprint)

db.init_app(app)
migrate.init_app(app, db)

# print(app.url_map)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    return response