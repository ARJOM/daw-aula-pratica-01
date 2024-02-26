import random
from flask import Flask, render_template, redirect, request

from db import listar_boardgames, remove_boardgame, novo_boardgame, detalha_boardgame, atualiza_boardgame

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
@app.route("/remover/<int:chave>")
def apagar(chave):
    remove_boardgame(chave)
    return redirect('/boardgames')

@app.route("/novo", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        novo_boardgame(dados.get('nome'), dados.get('duracao'), dados.get('min'), dados.get('max'), dados.get('ideal'))
        return redirect('/boardgames')
    return render_template('form_boardgame.html', jogo=None, title='Novo Jogo')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualiza_boardgame(chave, dados.get('nome'), dados.get('duracao'), dados.get('min'), dados.get('max'), dados.get('ideal'))
        return redirect('/boardgames')
    jogo = detalha_boardgame(chave)
    return render_template('form_boardgame.html', jogo=jogo, title='Editar Jogo')



if __name__ == '__main__':
    # Execução do servidor flask
    app.run()
