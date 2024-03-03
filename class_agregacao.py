# Agragação

class CarrinhoDeCompras:
    def __init__(self) -> None:
        self._produtos = []
    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

carrinho = CarrinhoDeCompras()

p1 = Produto('caneta', 2)
p2 = Produto('camisa', 30)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())