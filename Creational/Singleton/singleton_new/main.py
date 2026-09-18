# Importa a classe responsável pela conexão com o banco de dados.
from conexao_db import ConexaoDB


# Cria a primeira referência para ConexaoDB.
a = ConexaoDB()

# Cria uma segunda referência para ConexaoDB.
b = ConexaoDB()

# Verifica se as duas referências apontam para o mesmo objeto.
print(a is b)

# Executa uma consulta através da primeira referência.
print(a.consultar("SELECT * FROM acervo"))

# Executa uma consulta através da segunda referência.
print(b.consultar("SELECT * FROM acervo"))