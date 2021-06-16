from flask.helpers import url_for
from flask_login.utils import login_required, logout_user
from app import app
from flask import Flask, request, render_template, flash, redirect
# from Steganography import app
from forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data().first())
        if user is None or not user.check_password(form.password.data()):
            flash(f"Invalid Username or Password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title = "Sign In", form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
# @login_required left off here
def index():
    return render_template("index.html", title="Sign In")