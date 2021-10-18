from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# https://docs.sqlalchemy.org/en/13/orm/session_api.html#sqlalchemy.orm.session.Session.params.autoflush
db = SQLAlchemy(session_options={"autoflush": False, "autocommit": False})

migrate = Migrate()
