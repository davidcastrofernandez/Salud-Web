from flask import Flask,render_template,request,redirect

import socket 
app = Flask(__name__)
cedula=""
ip='192.168.1.130'



persona1 ={
        "5591945": {
                "nombre":"Mauricio",
                "apellido": "Acosta",
                "fecha_de_nacimiento":"23-12-2002",
                "sexo":"m",
                "ciudad":"San_Antonio",
                "grupo_sanguineo":"positivo",
                "telefono":"98768785",
                "vacunas":[
                    {"fecha":"18-06-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"28-10-2020"},
                    {"fecha":"23-03-2018","vacuna_aplicada":"antirabico","proxima_vacuna":"18-08-2019"},
                    {"fecha":"13-07-2019","vacuna_aplicada":"antitetanico","proxima_vacuna":"20-02-2019"}
                    ]
                }, 
        
        "982145358":{
                "nombre":"paula",
                "apellido": "santacruz",
                "fecha_de_nacimiento":"24-09-2002",
                "sexo":"f",
                "ciudad":"capiata",
                "grupo_sanguineo":"positivo",
                "telefono":"765765",
                "vacunas":[
                    {"fecha":"10-08-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"10-08-2020"},
                    {"fecha":"26-12-2019","vacuna_aplicada":"viruela","proxima_vacuna":"28-10-2020"},
                    {"fecha":"13-02-2019","vacuna_aplicada":"hepatitis","proxima_vacuna":"28-10-2020"}]
                }


}
               
"""
persona = [
    {
    "cedula":5591945,
    "nombre":"Mauricio",
    "apellido": "Acosta",
    "fecha_de_nacimiento":"23-12-2002",
    "sexo":"m",
    "ciudad":"San_Antonio",
    "grupo_sanguineo":"positivo",
    "telefono":"98768785",
    "vacunas":[
        {"fecha":"18-06-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"28-10-2020"},
        {"fecha":"23-03-2018","vacuna_aplicada":"antirabico","proxima_vacuna":"18-08-2019"},
        {"fecha":"13-07-2019","vacuna_aplicada":"antitetanico","proxima vacuna":"20-02-2019"}
        ]
    },
    {
    "cedula": 6970882,
    "nombre": "laura",
    "apellido": "Acosta",
    "fecha_de_nacimiento":"23-12-2002",
    "sexo":"m",
    }
]    

database = {
    "5591945":{"nombre":"Mauricio","apellido": "Acosta","fecha_de_nacimiento":"23-12-2002","sexo":"m",
    "ciudad":"San_Antonio","grupo_sanguineo":"positivo","telefono":"98768785",
    "vacunas":[
        {"fecha":"18-06-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"28-10-2020"},
        {"fecha":"23-03-2018","vacuna_aplicada":"antirabico","proxima_vacuna":"18-08-2019"},
        {"fecha":"13-07-2019","vacuna_aplicada":"antitetanico","proxima vacuna":"20-02-2019"}
        ]
    },
    {
    "cedula":982145358,
    "nombre":"paula",
    "apellido": "santacruz",
    "fecha_de_nacimiento":"24-09-2002",
    "sexo":"f",
    "ciudad":"capiata",
    "grupo_sanguineo":"positivo",
    "telefono":"765765",
    "vacunas":[
        {"fecha":"10-08-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"10-08-2020"},
        {"fecha":"26-12-2019","vacuna_aplicada":"viruela","proxima_vacuna":"28-10-2020"},
        {"fecha":"13-02-2019","vacuna_aplicada":"hepatitis","proxima_vacuna":"28-10-2020"}]
    },
    {
    "cedula":972543207,
    "nombre":"laura",
    "apellido": "gomez",
    "fecha_de_nacimiento":"27-04-2019",
    "sexo":"f",
    "ciudad":"villa ygatimi",
    "grupo_sanguineo":"0+",
    "telefono":"765765",
    "vacunas":[
        {"fecha":"16-09-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"11-08-2020"},
        {"fecha":"16-12-2019","vacuna_aplicada":"viruela","proxima_vacuna":"20-10-2020"},
        {"fecha":"19-02-2019","vacuna_aplicada":"hepatitis","proxima_vacuna":"24-10-2020"}]
    },
    {
    "cedula":98375984,
    "nombre":"david",
    "apellido": "castro",
    "fecha_de_nacimiento":"06-05-1994",
    "sexo":"m",
    "ciudad":"Chaco",
    "grupo_sanguineo":"0+",
    "telefono":"765765",
    "vacunas":[
        {"fecha":"10-08-2019","vacuna_aplicada":"antigripal","proxima_vacuna":"10-08-2020"},
        {"fecha":"26-12-2019","vacuna_aplicada":"viruela","proxima_vacuna":"28-10-2020"},
        {"fecha":"13-02-2019","vacuna_aplicada":"hepatitis","proxima_vacuna":"28-10-2020"}]
    }

]  

"""
#print(database["5591945"]["nombre"])
@app.route("/datos/<string:cedula>/")
def datos(cedula):
    return render_template("datos.html",paciente=persona1[cedula],cedula=cedula)

@app.route("/",methods=['GET','POST'])
def for_home():
    local="http://127.0.0.1:5000/datos/"
    if request.method=='POST':
        cedula=request.form.get('cedula')
        return redirect("http://127.0.0.1:5000/datos/"+cedula)
    return render_template("index.html",cedula="5591945")

@app.route("/vacuna/<string:cedula>/")
def vacuna_html(cedula):
    return render_template("vacuna.html",paciente=persona1[cedula],cedula=cedula)

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
        persona1[cedula]=diccionario
       
        redireccionar="http://"+ip +"/datos/"
        local="http://127.0.0.1:5000/datos/"
        print(redireccionar)
        return redirect(local+cedula)
    return render_template("registro.html")


@app.route("/registro")
def registro_html():
    return render_template("registro.html")
"""
@app.route("/",methods=['GET','POST'])
def for_registro():
    if request.method=='POST':
        Regiatro=request.form.get('cedula')
        return redirect("http://127.0.0.1:5000/datos/"+cedula)
    return render_template("index.html",cedula="5591945")
    """
if __name__=='__main__':
    ip='192.168.1.130'
    app.run(host=ip)
