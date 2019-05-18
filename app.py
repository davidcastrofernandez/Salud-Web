from flask import Flask,render_template
app = Flask(__name__)

database = {
    "5591945":{"nombre":"Mauricio","apellido": "Acosta","fecha_de_nacimiento":"23-12-2002","sexo":"m",
    "ciudad":"San_Antonio","grupo_sanguineo":"positivo","telefono":"98768785",
    "vacunas":[
        {"fecha":"18-06-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"28-10-2020"},
        {"fecha":"23-03-2018","vacuna_aplicada":"antirabico","proxima_vacuna":"18-08-2019"},
        {"fecha":"13-07-2019","vacuna_aplicada":"antitetanico","proxima vacuna":"20-02-2019"}
        ]
    },
    "6970882":{"nombre":"laura","apellido": "gomez","fecha_de_nacimiento":"27-04-2002","sexo":"f","ciudad":"Villa_Ygatimi","grupo_sanguineo":"ARH+ +","telefono":"8678858678",
    "vacunas":[
        {"fecha":"13-09-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"13-09-2020"},
        {"fecha":"09-06-2016","vacuna_aplicada":"antitetanos","proxima_vacuna":"06_09-2022"},
        {"fecha":"18-06-2019","vacuna_aplicada":"culebrilla","proxima_vacuna":"04-10-2020"}
    ]
    },
    "4238240":{"nombre":"David", "apellido": "Castro","fecha_de_nacimiento":"03-06-1993","sexo":"m",
    "ciudad":"chaco","grupo_sanguineo":"ARH+","telefono":"9878996",
    "vacunas":[
        {"fecha":"10-08-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"10-08-2020"},
        {"fecha":"26-12-2019","vacuna_aplicada":"viruela","proxima_vacuna":"28-10-2020"},
        {"fecha":"13-02-2019","vacuna_aplicada":"hepatitis","proxima_vacuna":"28-10-2020"}
    ]
    }
}
#print(database["5591945"]["nombre"])
@app.route("/datos/<string:cedula>/")
def datos(cedula):
    return render_template("datos.html",paciente=database[cedula],cedula=cedula)

@app.route("/")
def adios_html():
    return render_template("index.html",cedula="5591945")

@app.route("/vacuna/<string:cedula>/")
def vacuna_html(cedula):
    return render_template("vacuna.html",paciente=database[cedula],cedula=cedula)

@app.route("/historial")
def historial_html():
    return render_template("historial.html")

@app.route("/estudio")
def estudi_html():
    return render_template("estudio.html")

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
