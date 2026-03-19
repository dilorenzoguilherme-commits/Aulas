extrato = []
saldo = 0
while True:
    print("digite 1 - para deposito: ")
    print("digite 2 - para saque: ")
    print("digite 3 - para extrato: ")
    print("digite 4 - para sair: ")

    opcao = input("digite a operção que vai querer fazer: ")


    if opcao == '1':
        
            deposito = float(input("digite valor que quer depositar: "))
            
            saldo+=deposito

            print("deposito efetuado")
            extrato.append({"descricao": "deposito", "valor": deposito})

    elif opcao == '2':
         
         saque = float(input("digite valor que quer sacar: "))

         saldo -= saque

         print("saque efetuado ")
         extrato.append({"descricao": "Saque", "valor": -saque})
     
    elif opcao == '3':
          print("\n=== Extrato Bancário ===")
          for transacao in extrato:
            print(f"{transacao['descricao']}: R$ {transacao['valor']:.2f}")
          print(f"\nSaldo atual: R$ {saldo:.2f}\n")
          

    elif opcao == '4':
        print("encerrado")
        break