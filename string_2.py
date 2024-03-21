nome = "Wellington"
idade = 34
profissao = "Desenvolvedor e Engenheiro civil"
linguagem = "Python e Java"
saldo = 50.550

dados = {"nome": "Wellington", "idade": 34, "saldo": 50.550}

print("Nome: %s Idade: %d" % (nome, idade)) # Método old style (usando %)
print("Nome: {} Idade: {}".format(nome, idade)) # método format padrão
print("Nome: {1} Idade: {0}".format(idade, nome)) # método format com índice
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) # método format
print("Nome: {nome} Idade: {idade}".format(**dados)) # método format com biblioteca
print(f"Nome: {nome} Idade: {idade}") # método f-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}") # método f-string com biblioteca
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}") # formatando com f-string