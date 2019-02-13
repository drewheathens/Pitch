from flask import Flask
<<<<<<< HEAD
from config import config_options, Config
=======
from config import *
>>>>>>> 0d40a78dc1505fb4a4dcabc5ff2491f48afa6777
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

<<<<<<< HEAD
# mail = Mail()
#
# def create_app(config_name):
#
#     app = Flask(__name__)
#
#     # Creating the app configurations
#     app.config.from_object(config_options[config_name])
#     app.config.from_object(Config)
#
#
#     # Initializing flask extensions
#     bootstrap.init_app(app)
#     db.init_app(app)
#     mail.init_app(app)
#     login_manager.init_app(app)
#
#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
#
#
#     # Will add the views and forms
#
#     # Registering the blueprint
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#
#     # setting config
#     from .requests import configure_request
#     configure_request(app)
#
#     return app
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)

    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    # initializing flask login extension
    login_manager.init_app(app)

    #registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    #initializing the app with the flask extensions
=======
def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')


    # Will add the views and forms

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

>>>>>>> 0d40a78dc1505fb4a4dcabc5ff2491f48afa6777
    return app
