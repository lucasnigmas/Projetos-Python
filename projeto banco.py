menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque_diario = 500
extrato = ""
numero_saque_diarios = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        try:
            valor = float(input("informe o valor do deposito: "))
        
            if valor > 0:
                 saldo += valor
                 extrato += f"Deposito: R$ {valor:.2f}\n"
                 print("Depósito realizado com sucesso!")     
            else:
                 print("Operação falhou! O valor informado é inválido. Digite um valor positivo")
        except ValueError:
            print("Operação falhou! O valor informado não é um numero válido.")

    elif opcao == "s":
        try:
            valor = float(input("informe o valor do saque: "))

            if valor > saldo:
               print("operação falhou! você não tem saldo suficiente.")
               
            elif valor > limite_saque_diario:
                 print("Operação falhou! O valor do saque excede o limite.")

            elif numero_saque_diarios >= LIMITE_SAQUES:
                print("Operção falhou! Número máximo de saques diários excedido.")

            elif valor <= 0:
                print("Operação falhou! O valor informado é invalido. Digite um valor positivo")

        else: 
                saldo -= valor            
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saque_diarios += 1
                print("Saque realizado com sucesso!")

        except ValueError:
            print("Operação falhou! O valor informado não é m número válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
         else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}") 
        print("==========================================")

    elif opcao == "q":
        break   

    else: print("operação invalida, por favor selecione novamente a operação desejada.")    