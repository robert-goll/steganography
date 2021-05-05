from flask import Flask, request, render_template

app = Flask(__name__, static_folder="static")

@app.route("/")
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
    return render_template("index.html", title = "Starship SN15 wont RUD", posts = posts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8081', debug=True)