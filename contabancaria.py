#!/usr/bin/python3



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    print("""
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
    """)
    
    opcao = input("Opção: ").upper()
    
    if opcao == "D":
        
        valor = input("Depositar: ")
        valor = float(valor)
        saldo += valor
            
    
    elif opcao == "S":
        
        sacar = input("Sacar: ")
        sacar = float(sacar)
        
        if saldo == 0:
            print("\nSaldo insuficiente!")
            
        elif sacar > limite:
            print(f"\nAtenção!\nVocê ultrapassou o limite de saque R${limite}.")
     
     
        elif sacar <= limite:
            if numero_saques <= 2:
                saldo -= sacar
                numero_saques += 1
                print("\nSaque efetuado com sucesso!")
            
            else:
                print(f"\nAtenção! Você excedeu o limite {numero_saques}x\npara saques durante o dia.")
                print("Tente novamente amanhã")
        
                
     
     
    elif opcao == "E":
        print("\nExtrato da conta")
        extrato = f"Saldo: R${saldo:.2f}"
        print(extrato)
    
    elif opcao == "Q":
        break
   
    else:
        print("Opção Inválido!")    



