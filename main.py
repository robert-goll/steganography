from flask import Flask, request, render_template, flash, redirect
# from Steganography import app
from forms import LoginForm

app = Flask(__name__, static_folder="static")

app.config["SECRET_KEY"] = "just testing"

@app.route("/", methods=["GET", "POST"])
def index():
    posts = [
        {
            "author": {"name" : "SN15"},
            "body": {"Hoppy is the greatest starship ever"}
        },
        {
            "author": {"name" : "Hoppy"},
            "body": {"SN15 is the greatest other starship ever"}
        }
    ]
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user{form.username.data}, remember_me={form.remember_me.data}")
        return redirect("/index")
    return render_template("login.html", title = "Starship SN15 wont RUD", form = form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8081', debug=True)