from flask import Flask, render_template, request

app = Flask("app")

@app.route("/")
def homePage():
    return render_template("homePage.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/termos-de-uso")
def termosDeUso():
    return render_template("termosDeUso.html")

@app.route("/politica-de-privacidade")
def politicaDePrivacidade():
    return render_template("politicaPrivacidade.html")

@app.route("/como-utilizar")
def comoUtilizar():
    return render_template("comoUtilizar.html")