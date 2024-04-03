<<<<<<< HEAD
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#exemplo usando iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print() #adiciona uma quebra de linha
    print("Executa no final do laço")

#exemplo utilizando a função built-in range
for numero in range(0, 51, 5 ):
    print(numero, end="-")
=======
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#exemplo usando iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print() #adiciona uma quebra de linha
    print("Executa no final do laço")

#exemplo utilizando a função built-in range
for numero in range(0, 51, 5 ):
    print(numero, end="-")
>>>>>>> bac57c83c6f4f7e006e9f6b0d9695dc37a05a99a
