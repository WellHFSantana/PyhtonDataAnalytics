#exemplo 1
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

#exemplo 2
opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar\n [2] Extrato\n [0] Sair\n: "))

    if opcao == 1:
        print("Sacando...")
    
    elif opcao == 2:
        print("Exibindo extrato...")

    else:
        print("Obrigaod por usar nosso sistema bancário, até logo!")

#exemplo 3

for num in range(100):

    if num == 10:
        break

    print(num)

#exemplo 4

for num in range(100):

    if num == 10:
        continue

    print(num, end=" ")

#exemplo 5

for num in range(100):

    if num % 2 == 10:
        continue

    print(num, end=" ")