import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(
    description="Description",
    title="API",
    doc="/documentation/",
    validate=True,
)
