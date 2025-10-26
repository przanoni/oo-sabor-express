from modelos.restaurante import Restaurante

restaurante_sukiaki = Restaurante('Sukiaki', "Japonês")
restaurante_joana = Restaurante('Joana', 'Brasileira')
restaurante_mineiro = Restaurante('Tempero Mineiro', 'Mineira')
restaurante_joana.receber_avaliacao('Paulo', 10)
restaurante_joana.receber_avaliacao('Lais', 5)
restaurante_joana.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
