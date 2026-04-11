from flask import Flask
from .models import db
from .config import Config

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .blueprints.users  import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from .blueprints.notes import notes_bp
    app.register_blueprint(notes_bp, url_prefix='/notes')


    return app