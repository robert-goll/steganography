from app import app
from flask import Flask, request, render_template, flash, redirect
# from Steganography import app
from forms import LoginForm

@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user{form.username.data}, remember_me={form.remember_me.data}")
        return redirect("/index")
    return render_template("login.html", title = "Starship SN15 wont RUD", form = form)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    return render_template("index.html", title="I was right:)")