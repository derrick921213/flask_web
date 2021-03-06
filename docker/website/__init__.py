from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from datetime import timedelta
from werkzeug.security import generate_password_hash
import os
import yaml

app = Flask(__name__)
jwt = JWTManager()
app.config['SECRET_KEY'] = 'dfjsiojeifkjdks iejridkfsleklj kmdskljlkemf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'dlkfokeokofsjopodkfopeoieljmiopfjfffd'
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=2)
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['JWT_QUERY_STRING_NAME'] = 'token'
db = SQLAlchemy(app)
jwt.init_app(app)


def setting():
    if os.path.isfile(os.path.dirname(__file__)+'/conf/setting.yaml'):
        with open(os.path.dirname(__file__)+'/conf/setting.yaml', 'r') as f:
            settings = yaml.load(f)
            return settings
    else:
        init_config()
        print('Create Seccuss')


def init_config():
    setting = dict(extra_file_location='extra_web', admin_email='admin@gmail.com',
                   admin_user='admin', password='1234567')
    with open(os.path.dirname(__file__)+'/conf/setting.yaml', 'w') as f:
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

    @ login_manger.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    from .models import User
    if not path.exists('website/database.db'):
        db.create_all(app=app)
        db.session.commit()
        settings = setting()
        email = settings['admin_email']
        username = settings['admin_user']
        passwd = settings['password']
        new_user = User(email=email, first_name=username, password=generate_password_hash(
            passwd, method='sha256'), level=1)
        db.session.add(new_user)
        db.session.commit()
        print('Created Database!')
    # else:
        #settings = setting()
        #email1 = settings['admin_email']
        #user_name = settings['admin_user']
        #passwd = settings['password']
        #user = User.query.filter_by(email='admin@gmail.com').first()
        #user.email = email1
        #user.password = generate_password_hash(passwd, method='sha256')
        #user.first_name = user_name
        # db.session.commit()
