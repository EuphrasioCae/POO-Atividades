from modelos.cardapio.item_cardapio import ItemCardapio

# Essa classe é filha de ItemCardapio -Herdando todos os parâmetros dela-
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
    