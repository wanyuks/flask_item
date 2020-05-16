# from flask_mail import Mail
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
# mail = Mail()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db=db)
    # mail.init_app(app)
    # Session(app)
