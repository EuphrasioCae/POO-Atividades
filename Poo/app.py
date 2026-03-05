from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
restaurante_praca.adicionar_no_cardapio(bebida_suco)

prato_paozinho = Bebida('Paozinho', 2.0, 'O melhor da cidade')
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()