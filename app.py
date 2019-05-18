from flask import Flask,render_template,request
app = Flask(__name__)
cedula=""
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

@app.route("/",methods=['GET','POST'])
def for_home():
    if request.method=='POST':
        cedula=request.form.get('cedula')
        return render_template("index.html",cedula=cedula)
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

@app.route("/formulario",methods=['GET','POST'])
def for_preguntas():
    if request.method=='POST':
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        fecha_de_nacimiento=request.form.get('fecha_de_nacimento')
        sexo=request.form.get('sexo')
        ciudad=request.form.get('ciudad')
        grupo_sanguineo=request.form.get('grupo_sanguineo')
        telefono=request.form.get('telefono')
        cedula=request.form.get('cedula')
        diccionario={}
        diccionario["nombre"]= nombre
        diccionario["apellido"]= apellido
        diccionario["fecha_de_nacimiento"]=fecha_de_nacimiento
        diccionario["sexo"]= sexo
        diccionario["ciudad"]= ciudad
        diccionario["grupo_sanguineo"]= grupo_sanguineo
        diccionario["telefono"]= telefono
        diccionario["vacunas"]=[]
        database[cedula]=diccionario
        return render_template("index.html",cedula=cedula)
    return render_template("index.html",cedula="5591945")
       




