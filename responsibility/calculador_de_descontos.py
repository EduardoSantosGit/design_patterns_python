from responsibility.orcamento import Orcamento,Item
from responsibility.descontos import Desconto_por_cinco_itens,Desconto_por_mais_de_quinhentos_reais,Sem_desconto

class Calculador_de_descontos(object):


    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        )

        return desconto.calcula(orcamento)

if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print ('Desconto calculado : %s' % (desconto))
    # imprime 38.5