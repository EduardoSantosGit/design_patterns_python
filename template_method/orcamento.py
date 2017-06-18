class Orcamento(object):

    def __init__(self,valor):

        self.__valor = valor #__ faz a variavel ficar privada

    #chama properti quando chama valor
    @property
    def valor(self):
        return self.__valor