class Usuario:
    def __init__(self, nome, dataNascimento, cpf, logadouro, bairro, cidade, estado):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.endereco = {
            "logadouro": logadouro,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }