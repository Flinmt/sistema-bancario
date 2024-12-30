class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_de_saque = 3

    def deposito(self):
        valor = float(input("Digite o valor do deposito: R$"))
        if (valor > 0):
            self.saldo += valor
            self.extrato.append(f"Deposito --- R${valor:.2f}")
            return "Deposito realizado com sucesso."
        return "Insira um valor valido!"

    def saque(self):
        print("_______________________________________")
        if self.limite_de_saque <= 0: 
            print("Lamento, você estourou o limite de saques de hoje.") 
            return
        if self.saldo == 0: 
            print("Você não possui saldo suficiente")
            return
        
        valor = float(input("Digite o valor do saque: R$"))
        if valor <= 0 or valor > 500: 
            print("O valor do saque deve ser maior que R$0,00 e menor que R$500,00")
            return
        if valor > self.saldo: 
            print("Saldo insuficiente, cancelando operação.")
            return

        self.saldo -= valor
        self.extrato.append(f"Saque --- R${valor:.2f}")
        self.limite_de_saque -= 1
        print("Saque realizado com sucesso!")


    def mostrar_extrato(self):    
        print("_______________________________________")
        if not self.extrato: 
            print("Não foram realizadas movimentações")
            return
        for conta in self.extrato:
            print(conta)

def main():
    conta = Conta()
    switch = 0

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