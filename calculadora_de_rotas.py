class Rotas:
    def __init__(self):
        self.rotas = {}

    def adicionar_rota(self, origem, destino, valor):
        if origem not in self.rotas:
            self.rotas[origem] = {}
        self.rotas[origem][destino] = valor

    def adicionar_rotas(self, rotas):
        for origem, destinos in rotas.items():
            for destino, valor in destinos.items():
                self.adicionar_rota(origem, destino, valor)

    def get_rotas(self):
        return self.rotas


class Rota:
    def __init__(self):
        self.rotas = {}

    def adicionar_rota(self, origem, destino, valor):
        if origem not in self.rotas:
            self.rotas[origem] = {}
        self.rotas[origem][destino] = valor

    def valor_rota(self, caminho):
        valor_total = 0
        for i in range(len(caminho)-1):
            origem = caminho[i]
            destino = caminho[i+1]
            if origem in self.rotas and destino in self.rotas[origem]:
                valor_total += self.rotas[origem][destino]
            else:
                return None
        return valor_total

