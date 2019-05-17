from flask import Flask,render_template
app = Flask(__name__)

@app.route("/hola")
def render_html():
    return render_template("index.html")
