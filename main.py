'''
leia do teclado uma distância em quilômetros e mostre na tela o seu valor convertido em metros.
(Valores inválidos: números negativos).


leia do teclado uma distância em metros e mostre na tela o seu valor convertido em quilômetros.
(Valores inválidos: números negativos).

'''


class Distancia:
    """
    Trata o valor da distancia fornecida
    """
    def __init__(self):
        self.distancia = -1

    def set_distancia(self):
        """
        Usuario insere um valor float referente a uma distancia que seja >=0
        """
        while self.distancia < 0:
            self.distancia = float(input('Insira um valor da distancia: \n'))
            if self.distancia < 0:
                print('Valores inválidos: números negativos\n')

    def converter_metro(self):
        """
        Converte o valor em metros.
        :return: retorna um float do valor em metros
        """
        metros = self.distancia * 1000
        return metros

    def converter_kilometros(self):
        """
        Converte o valor em kilometros.
        :return: retorna um float do valor em kilometros
        """
        kilometros = self.distancia / 1000
        return kilometros


d = Distancia()
d.set_distancia()
print(f'O valor representa {d.converter_metro():.2f} metros.')
print(f'O valor representa {d.converter_kilometros():.3f} kilometros.')
