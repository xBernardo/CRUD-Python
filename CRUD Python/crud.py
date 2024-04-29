import mysql.connector

# Script de CRUD, que permite criar, ler, atualizar, excluir infomações de uma tabela MySQL
# Obs: Ao rodar o códido desta maneira vai possuir um erro, pois vai dar conflitos entres o CRUD
# Antes de fazer a consulta, comentar os outros elementos do CRUO

conexão = mysql.connector.connect(
    host='localhost',    # Local onde o programa está sendo executado
    user='root',         # Usuário do sistema
    password='1234',     # Senha informada no seu root
    database='bdcrud',   # Schema criado no seu WorkBench
)

cursor = conexão.cursor()

# CREATE
# Responsável por criar novos registros ou entradas de um banco de dados

nome_produto = "Papel"
valor = 12
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexão.commit() #Editando o bando de dados
#resultado = cursor.fetchall() #Lendo o banco de dados


#READ
# Responsável pela leitura de informações existentes no banco de dados

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
#Conexão.commit() #Editando o bando de dados
resultado = cursor.fetchall() #Lendo o banco de dado
print(resultado)


# UPDATE
# Responsável por atualizar ou modificar elementos de um banco de dados

nome_produto = "Café"
valor = 8
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexão.commit() #Editando o bando de dados


# DELETE
#Responsável pela exclusão de informações existentes no banco de dados

nome_produto = "Papel"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexão.commit() #Editando o bando de dados

cursor.close()
conexão.close()