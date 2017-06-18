from template_method.impostos import ISS, ICMS,ICPP,IKCV
from template_method.orcamento import Orcamento

'''template method'''

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print (valor)

if __name__ == '__main__':
    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()

    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    calculador_de_impostos.realiza_calculo(orcamento, IKCV())
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
