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
