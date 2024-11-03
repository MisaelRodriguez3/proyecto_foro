from flask import Flask
from .routes import register_routes
from .models import db
from .utils import login_manager
from flask_migrate import Migrate

app = Flask(__name__)

def run_server(config):
    #Configuration
    app.config.from_object(config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_client.login_page'
    migrate = Migrate(app, db)

    #Blueprints
    register_routes(app)

    #Crear tablas
    with app.app_context():
        db.create_all()
    return app