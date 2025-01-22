from src.model.conta import Conta
from src.model.usuario import Usuario

def cadastrarUsuario():
    a

def main():
    
    switch = 0
    while (True):
        print("_______________________________________")
        print("Olá! Bem vindo(a) ao Nosso Banco.")
        print("1: Realizar Login.")
        print("2: Cadastrar Novo Usuario.")
        print("3: Cadastrar Nova Conta Corrente")
        print("0: Encerrar")
        print("_______________________________________")
    
        try:
            switch = int(input("Selecione uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue
        
        if switch == 1: conta.deposito()
        if switch == 2: conta.saque()
        if switch == 3: conta.mostrar_extrato()
        if switch == 0: break
        
    conta = Conta()
    while (True):
        print("_______________________________________")
        print("Olá! Bem vindo(a) ao Nosso Banco.")
        print(f"==== SALDO: R${conta.saldo:.2f} ====")
        print("1: Deposito")
        print("2: Saque")
        print("3: Extrato")
        print("0: Encerrar")
        print(f"==== LIMITE DE SAQUES: {conta.limite_de_saque} ====")
        print("_______________________________________")
        
        try:
            switch = int(input("Selecione uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue
        
        if switch == 1: conta.deposito()
        if switch == 2: conta.saque()
        if switch == 3: conta.mostrar_extrato()
        if switch == 0: break
        print("_______________________________________")
    print("_______________________________________")
    print("Adeus, foi um prazer ajuda-lo(a)!")
     
if __name__ == "__main__": 
    main()