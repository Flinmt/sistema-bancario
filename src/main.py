from model.usuario import Usuario
from datetime import datetime
import sys

def main():
    usuarios = []
    
    def cadastrarUsuario():
        print("_______________________________________")
        nome = input("Digite seu Nome: ").strip()
        cpf = input("Digite seu CPF: ").strip()

        # Verifica se o CPF já está cadastrado
        for usuario in usuarios:
            if usuario.cpf == cpf:
                print("Erro: CPF já cadastrado!")
                return
        
        logradouro = input("Digite a rua onde você mora: ").strip()
        bairro = input("Digite seu Bairro: ").strip()
        cidade = input("Digite sua Cidade: ").strip()
        estado = input("Digite a sigla do seu Estado: ").strip().upper()

        # Validação da data de nascimento
        while True:
            data = input("Digite sua data de nascimento (dd/mm/aaaa): ").strip()
            try:
                data_formatada = datetime.strptime(data, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Formato de data inválido! Use dd/mm/aaaa.")
        
        usuarios.append(Usuario(nome, data_formatada, cpf, logradouro, bairro, cidade, estado))
        print("Usuário cadastrado com sucesso!")
        print("_______________________________________")
        
    def login():
        print("_______________________________________")
        cpf = input("Digite seu CPF: ").strip()
        
        for usuario in usuarios:
            if usuario.cpf == cpf:
                return usuario  # Retorna o usuário encontrado
        
        print("Usuário não encontrado.")
        return None
    
    while True:
        print("_______________________________________")
        print(f"Olá! Bem-vindo(a) ao Nosso Banco.")
        print("1: Cadastrar Usuário")
        print("2: Realizar Login")
        print("0: Encerrar")
        print("_______________________________________")
        
        try:
            switch = int(input("Selecione uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue
        
        if switch == 1:
            cadastrarUsuario()
        elif switch == 2:
            logado = login()
            if logado:
                break  # Sai do loop caso o login seja bem-sucedido
        elif switch == 0:
            sys.exit()  # Encerra o programa corretamente
        else:
            print("Opção inválida, tente novamente.")
    
    while True:
        print("_______________________________________")
        print(f"Olá {logado.nome}! Bem-vindo(a) ao Nosso Banco.")
        print(f"==== SALDO: R${logado.conta.saldo:.2f} ====")
        print("1: Depósito")
        print("2: Saque")
        print("3: Extrato")
        print("0: Encerrar")
        print(f"==== LIMITE DE SAQUES: {logado.conta.limite_de_saque} ====")
        print("_______________________________________")
        
        try:
            switch = int(input("Selecione uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue
        
        if switch == 1:
            logado.conta.deposito()
        elif switch == 2:
            logado.conta.saque()
        elif switch == 3:
            logado.conta.mostrar_extrato()
        elif switch == 0:
            sys.exit()  # Encerra corretamente
        else:
            print("Opção inválida, tente novamente.")
        
        print("_______________________________________")

if __name__ == "__main__": 
    main()
