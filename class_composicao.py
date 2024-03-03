# composição

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando: ', self.nome)


class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua 
        self.numero = numero

    def __del__(self):
        print('Apagando: ', self.rua, self.numero)


cliente1 = Cliente('Giovani')
cliente1.inserir_endereco('Rua A', 9999)
cliente1.inserir_endereco('Rua B', 1111)
cliente1.listar_endereco()
# print(cliente1.enderecos[0].rua)

cliente2 = Cliente('João')
cliente2.inserir_endereco('Rua C', 1212)
cliente2.listar_endereco()

del cliente1

print(100 * '-')
