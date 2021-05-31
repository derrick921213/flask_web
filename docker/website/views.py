from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from . import db
from .models import *
from .getip import getip
from werkzeug.security import generate_password_hash, check_password_hash
from website import token_ar

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def home():
    return render_template("home.html", user=current_user, test=getip())
