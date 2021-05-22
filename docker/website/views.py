from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from . import db
from .models import *
from .getip import getip
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)


@views.route('/cgi-bin')
def cgi():
    return render_template("back.html", user=current_user, test=getip())


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user, test=getip())


@views.route('/back')
@login_required
def back():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if user.level == 1:
                return redirect(url_for('views.home'))
            else:
                return render_template('back.html', user=current_user)
    return render_template('back.html', user=current_user, test=getip())
