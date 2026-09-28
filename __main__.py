import sqlite3

def criar_tabela():
    banco = sqlite3.connect('crud.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), gmail VARCHAR(100))')
    banco.commit()
    banco.close()
    print("Tabela criada com ID automático!")
    
   
def adicionar(nome,gmail):
	   banco = sqlite3.connect('crud.db')
   	cursor = banco.cursor()
	   cursor.execute('INSERT INTO usuarios(nome,gmail) VALUES(?,?)', (nome, gmail))
	   banco.commit()
    banco.close()
	   print(f'{nome} foi add cm sucesso a lista')
	
def lista():
	   banco = sqlite3.connect('crud.db')
	   cursor = banco.cursor()
	   cursor.execute('SELECT * FROM usuarios')
	
	   for lista in cursor.fetchall():
		     print(f'{lista}')
	
	   banco.close()
	

def deletar(id):
	   banco = sqlite3.connect('crud.db')
	   cursor = banco.cursor()
	   try:
		     cursor.execute('DELETE  FROM  usuarios WHERE id = ?' ,(id,))
		     banco.commit()
		     banco.close()
		     print(f'id {id} deletado com sucesso ')
		
	   except:
		     print(f'O id {id} nao esta na lista')
		
		
#teste
if __name__ == '__main__':
	
  criar_tabela()	
	#adicionar('bruno', 'brunocarvalho de abreu lucas15@gmail.com')
		
#	deletar(id = 5)	
	 lista()
