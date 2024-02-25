import sqlite3


def cria_tabela():
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS boardgames(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            tempoDePartida VARCHAR(3) NOT NULL,
            minimoJogadores REAL NOT NULL,
            maximoJogadores REAL NOT NULL,
            idealJogadores REAL
        );
    """)

    conn.close()


def novo_boardgame(nome, tempoDePartida, min, max, ideal=None):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()

    if not ideal:
        ideal = 'Null'

    cursor.execute(f"""
        INSERT INTO boardgames(nome, tempoDePartida, minimoJogadores, maximoJogadores, idealJogadores)
        VALUES('{nome}', '{tempoDePartida}', {min}, {max}, {ideal});
    """)
    conn.commit()
    conn.close()


def listar_boardgames():
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM boardgames")
    resultado = []
    for item in values.fetchall():
        resultado.append({
            'id': item[0],
            'nome': item[1],
            'tempoDePartida': item[2],
            'minimoJogadores': item[3],
            'maximoJogadores': item[4],
            'idealJogadores': item[5]
        })
    print(resultado)
    conn.close()
    return resultado


def atualiza_boardgame(id, nome, tempoDePartida, min, max, ideal):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()
    cursor.execute(f"""
        UPDATE boardgames
        SET nome='{nome}', 
        tempoDePartida = '{tempoDePartida}', 
        minimoJogadores = {min}, 
        maximoJogadores = {max}, 
        idealJogadores = {ideal}
        WHERE id={id}
    """)
    conn.commit()
    conn.close()


def remove_boardgame(id):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()
    cursor.execute(f"""
        DELETE FROM boardgames
        WHERE id={id}
    """)
    conn.commit()
    conn.close()


def detalha_boardgame(id):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()
    value = cursor.execute(f"""
            SELECT * 
            FROM boardgames
            WHERE id={id}
        """)
    item = value.fetchone()
    conn.close()
    return {
        'id': item[0],
        'nome': item[1],
        'tempoDePartida': item[2],
        'minimoJogadores': item[3],
        'maximoJogadores': item[4],
        'idealJogadores': item[5]
    }


if __name__=='__main__':
    cria_tabela()
