import random
from flask import Flask, render_template, redirect

from db import listar_boardgames, remove_boardgame

# Criação de app
app = Flask(__name__)


# HTML em string
@app.route('/')
def hello_world():
    return """
        <h2>Olá Mundo</h2>
        <p>Este é um exemplo de flask</p>
        <ul>
            <li>Cliente</li>
            <li>Servidor</li>
        </ul>
    """


# Recebendo parâmetros da URL
@app.route('/oi/<string:nome>')
def oi(nome):
    return f"Fala tu {nome}!"


# Renderizando templates externos
@app.route('/template')
def template():
    return render_template('base.html', numero=random.randint(1, 999))


# Renderizando templates usando dados do banco
@app.route('/boardgames')
def list_boardgames():
    all_games = listar_boardgames()
    return render_template("boardgames.html", jogos=all_games)


# Recebendo parâmetro na url, execução de operação do banco e redirecionamento
@app.route("/apagar/<int:chave>")
def apagar(chave):
    remove_boardgame(chave)
    return redirect('/boardgames')


if __name__ == '__main__':
    # Execução do servidor flask
    app.run()
