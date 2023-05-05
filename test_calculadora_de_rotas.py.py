from calculadora_de_rotas import Rotas, Rota


def test_calculadora_rotas():
    rotas = Rotas()

    # Adiciona as rotas
    rotas.adicionar_rota('A', 'B', 10)
    rotas.adicionar_rota('B', 'C', 15)
    rotas.adicionar_rota('A', 'C', 20)
    rotas.adicionar_rota('C', 'D', 30)
    rotas.adicionar_rota('C', 'E', 35)

    # Cria a classe Rota e adiciona as rotas
    rota = Rota()
    rota.adicionar_rota('A', 'B', 10)
    rota.adicionar_rota('B', 'C', 15)
    rota.adicionar_rota('A', 'C', 20)
    rota.adicionar_rota('C', 'D', 30)
    rota.adicionar_rota('C', 'E', 35)

    # Testa a função valor_rota com algumas rotas
    assert rota.valor_rota(['A', 'B', 'C']) == 25
    assert rota.valor_rota(['A', 'C', 'E', 'B']) is None
    assert rota.valor_rota(['A', 'B', 'D']) is None

if __name__ == '__main__':
    test_calculadora_rotas()
    print('Todos os testes passaram.')
