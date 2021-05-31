from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .getip import getip
from .token_ar import refresh_token_get

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
                global tk_id
                tk_id = refresh_token_get(email)
                user.token = tk_id
                db.session.commit()
                flash('Logged in successfully!', category='success')
                login_user(user, fresh=False)
                return redirect(url_for('auth.back'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


def cheack():
    user = User.query.filter_by(email=login_email).first()
    if user.level == '1':
        return '1'
    else:
        return 'nopass'


@auth.route('/changepasswd', methods=['GET', 'POST'])
@login_required
def changepasswd():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            if len(password1) >= 7:
                if password1 == password2:
                    user.password = generate_password_hash(
                        password1, method='sha256')
                    db.session.commit()
                    flash('Password Changed!', 'SUCCESS')
                    return redirect(url_for('auth.login'))
                else:
                    flash('Passwords don\'t match.', 'error')
            else:
                flash('Passwords must be at least 7 characters.', 'error')
        else:
            flash('Email didn\'t exists.', category='error')
            return redirect(url_for('auth.login'))
    if 'login_email' in globals():
        user = User.query.filter_by(email=login_email).first()
        return render_template('changepwd.html', user=current_user, user_email=user.email)
    return redirect(url_for('auth.back'))


@auth.route('/back')
@login_required
def back():
    if 'login_email' in globals():
        identify = cheack()
        if identify == '1':
            return render_template('back.html', user=current_user, test=getip(), token_id=tk_id)
        else:
            return redirect(url_for('views.home'))
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    if 'login_email' in globals():
        user = User.query.filter_by(email=login_email).first()
        user.token = ''
        db.session.commit()
        logout_user()
        return redirect(url_for('auth.login'))
    amount = User.query.count()
    user = User.query.all()
    for i in range(0, amount):
        user[i].token = ''
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
            return redirect(url_for('auth.back'))
    return render_template("sign-up.html", user=current_user, sign="Add Users")


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
            return redirect(url_for('auth.back'))
    return render_template("sign-up.html", user=current_user, sign="Add admins")
