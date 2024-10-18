menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informar o valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Não é possível depositar valores negativos!!!")

    elif opcao == "s":
        valor = float(input("Informar o valor a ser sacado:"))
        
        excedeu_qntd_saques = numero_saques >= LIMITE_SAQUES

        excedeu_limite_diario = valor > limite

        excedeu_saldo_conta = valor > saldo

        if excedeu_limite_diario:
            print("Operação falhou! Número máximo de saques excedido.")

        elif excedeu_saldo_conta:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite_diario:
            print("Operação falhou! O valor do saque excede o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
