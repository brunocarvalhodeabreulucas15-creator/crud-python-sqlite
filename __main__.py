import sqlite3

def criar_tabela():
    banco = sqlite3.connect('crud.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), gmail VARCHAR(100))')
    banco.commit()
    banco.close()
    
def adicionar(nome, gmail):
    banco = sqlite3.connect('crud.db')
    cursor = banco.cursor()
    cursor.execute('INSERT INTO usuarios(nome, gmail) VALUES(?, ?)', (nome, gmail))
    banco.commit()
    banco.close()
    print(f'{nome} foi add com sucesso')

def lista():
    banco = sqlite3.connect('crud.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM usuarios')
    for l in cursor.fetchall():
        print(l)
    banco.close()

def deletar(id):
    banco = sqlite3.connect('crud.db')
    cursor = banco.cursor()
    try:
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
        banco.commit()
        print(f'id {id} deletado com sucesso')
    except:
        print(f'O id {id} nao esta na lista')
    finally:
        banco.close()

# teste
if __name__ == '__main__':
    criar_tabela()
    # adicionar('bruno', 'brunocarvalho@example.com')
    # deletar(id=5)
    lista()