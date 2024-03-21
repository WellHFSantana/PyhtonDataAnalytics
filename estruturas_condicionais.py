MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade "))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode retirar a CNH.")

if idade < MAIOR_IDADE:
    print("Não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior idade, pode retirar a CNH.")
else:
    print("Não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior idade, pode retirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Não pode tirar a CNH.")