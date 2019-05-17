from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return   """
        <h1>hello word</h1>
        <br />
        <p> This is Paragraph </p>   
"""
@app.route("/hola")
def render_html():
    return render_template("index.html")

@app.route("/adios")
def adios_html():
    return render_template("index.html")


@app.route("/usuario")
def render2_html():
    personainfo = {
        "nombre": "Juan",
        "edad":24
        }
    return personainfo["nombre"]

@app.route("/edad")
def edad():
    personainfo = {
        "nombre": "Juan",
        "edad":24
        }
    personainfo["edad"]=personainfo["edad"]+1   
    return str(personainfo["edad"])

@app.route("/info/<string:campo>/")
def nombre(campo):
    personainfo = {
        "nombre": "juan",
        "edad":24,
        "cedula":3667788,
        "telefono":982345345
        }
    return str(personainfo[campo])
