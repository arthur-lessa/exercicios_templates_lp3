from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
    { "nome": "Frutas Orgânicas", "descricao": "Frutas frescas cultivadas sem pesticidas ou fertilizantes químicos.", "img": "1" },
    { "nome": "Creme Facial Natural", "descricao": "Creme hidratante com óleo de rosa mosqueta e vitamina E, livre de parabenos e sulfatos.", "img": "2" },
    { "nome": "Suplemento de Vitamina C Orgânica", "descricao": "Cápsulas de vitamina C extraída de acerola, rica em antioxidantes naturais.", "img": "3" }
]

app = Flask("app")

@app.route("/")
def homePage():
    return render_template("homePage.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/cadastro", methods=['GET'])
def cadastro_produto():
    return render_template("cadastroProduto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = {"nome": nome,"descricao": descricao, "img": ''}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/cpf")
def cpf():
    cpf = CPF()
    cpfretorno = cpf.generate(True)
    return render_template("cpf.html", cpf = cpfretorno)
    return render_template("cadastro_produto.html")

@app.route("/cnpj")
def cnpj():
    cnpj = CNPJ()
    cnpjretorno = cnpj.generate(True)
    return render_template("cnpj.html", cnpj = cnpjretorno)

@app.route("/termos-de-uso")
def termosDeUso():
    return render_template("termosDeUso.html")

@app.route("/politica-de-privacidade")
def politicaDePrivacidade():
    return render_template("politicaPrivacidade.html")

@app.route("/como-utilizar")
def comoUtilizar():
    return render_template("comoUtilizar.html")