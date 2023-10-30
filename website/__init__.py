from config import Config
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .views import view
    from .views import about
    from .views import upload
    app.register_blueprint(view, url_prefix='/')

    return app

