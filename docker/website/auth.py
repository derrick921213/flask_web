from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .getip import getip
import secrets

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        global login_email
        login_email = email
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                user.token = secrets.token_urlsafe(10)
                db.session.commit()
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.back'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user, test=getip())


@auth.route('/logout')
@login_required
def logout():
    user = User.query.filter_by(email=login_email).first()
    user.token = ''
    db.session.commit()
    logout_user()

    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
@login_required
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must beer than 3 characters.', 'error')
        elif len(firstName) < 2:
            flash('First name must beer than 1 characters.', 'error')
        elif password1 != password2:
            flash('Passwords don\'t match.', 'error')
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters.', 'error')
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(
                password1, method='sha256'), level=0)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', 'SUCCESS')
            return redirect(url_for('views.back'))
    return render_template("sign-up.html", user=current_user, test=getip())


@auth.route('/add-admin', methods=['GET', 'POST'])
@login_required
def add_admin():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must beer than 3 characters.', 'error')
        elif len(firstName) < 2:
            flash('First name must beer than 1 characters.', 'error')
        elif password1 != password2:
            flash('Passwords don\'t match.', 'error')
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters.', 'error')
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(
                password1, method='sha256'), level=1)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', 'SUCCESS')
            return redirect(url_for('views.back'))
    return render_template("sign-up.html", user=current_user)
