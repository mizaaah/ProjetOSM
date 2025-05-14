from flask import Flask
from app.models import db
from app.routes import routes  
from app.config import Config

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(routes)

    return app