# Importa a classe de conexão.
from conexao_db import ConexaoDB


# Cria a primeira instância.
a = ConexaoDB()

# Cria a segunda instância.
b = ConexaoDB()

# Verifica se as duas referências apontam para o mesmo objeto.
print(a is b)

# Executa uma consulta através da primeira referência.
print(a.consultar("SELECT * FROM acervo"))

# Executa uma consulta através da segunda referência.
print(b.consultar("SELECT * FROM acervo"))