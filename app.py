from flask import Flask,render_template
app = Flask(__name__)

database = {
    "5591945":{"nombre":"Mauricio","apellido": "Acosta","fecha_de_nacimiento":"23-12-2002","sexo":"m","ciudad":"San_Antonio","grupo_sanguineo":"positivo","telefono":"98768785"},
    "6970882":{"nombre":"laura","apellido": "gomez","fecha_de_nacimiento":"27-04-2002","sexo":"f","ciudad":"Villa_Ygatimi","grupo_sanguineo":"ARH+ +","telefono":"8678858678"},
    "4238240":{"nombre":"David", "apellido": "Castro","fecha_de_nacimiento":"03-06-1993","sexo":"m","ciudad":"chaco","grupo_sanguineo":"ARH+","telefono":"9878996"}
}
#print(database["5591945"]["nombre"])
@app.route("/datos/<string:cedula>/")
def datos(cedula):
    return render_template("datos.html",paciente=database[cedula])


@app.route("/vacunacion/<string:campo>/")
def nombre(campo):
    return str(personainfo[campo])