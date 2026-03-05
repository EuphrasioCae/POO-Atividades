from modelos.cardapio.item_cardapio import ItemCardapio

# Essa classe é filha de ItemCardapio -Herdando todos os parâmetros dela-
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
    