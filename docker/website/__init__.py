from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from datetime import timedelta
from werkzeug.security import generate_password_hash
import os
import yaml

DB_NAME = "database.db"
app = Flask(__name__)
jwt = JWTManager()
app.config['SECRET_KEY'] = 'dfjsiojeifkjdks iejridkfsleklj kmdskljlkemf'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['JWT_SECRET_KEY'] = 'dlkfokeokofsjopodkfopeoieljmiopfjfffd'
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=2)
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['JWT_QUERY_STRING_NAME'] = 'token'
jwt.init_app(app)
db = SQLAlchemy(app)


def setting():
    if os.path.isfile('conf/setting.yaml'):
        with open('conf/setting.yaml', 'r') as f:
            settings = yaml.load(f)
            return settings
    else:
        init_config()
        print('Create Seccuss')


def init_config():
    setting = dict(extra_file_location='extra_web', admin_email='admin@gmail.com',
                   admin_user='admin', password='1234567')
    with open('conf/setting.yaml', 'w') as f:
        yaml.dump(setting, f, sort_keys=False)


def create_app():

    setting()

    from .views import views
    from .auth import auth
    from .token_ar import token

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(token, url_prefix='/')

    from .models import User
    create_database(app)

    login_manger = LoginManager()
    login_manger.login_view = 'auth.login'
    login_manger.init_app(app)

    @login_manger.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    from .models import User
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        settings = setting()
        new_user = User(email=settings['admin_email'], first_name=settings['admin_user'],
                        password=generate_password_hash(settings['password'], method='sha256'), level=1)
        db.session.add(new_user)
        db.session.commit()
        print('Created Database!')
