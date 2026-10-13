
from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    username = "Prathusha"
    today = date.today().strftime("%d-%m-%Y")
    items = ["Python", "Flask", "HTML", "CSS", "Jinja2"]

    return render_template(
        "home.html",
        username=username,
        today=today,
        items=items
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
