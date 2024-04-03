<<<<<<< HEAD
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450 

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")    

else: 
=======
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450 

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")    

else: 
>>>>>>> bac57c83c6f4f7e006e9f6b0d9695dc37a05a99a
    print("Sistema não reconheceu seu tipo de conta, entre em contado com o seu gerente:  ")