class Interseccao2:
    def __init__(self):
        self.direcao = {'2': -1, '3': -1, '5': -1}
        self.tentativas = -1
    def push(self, cor):
        self.direcao['{}'.format(cor)] = self.tentativas
        self.tentativas = -1
    def acessa(self, cor):
        return self.direcao['{}'.format(cor)]
    def processa(self):
        self.tentativas += 1
        return 0
    def __str__(self):
        return '{}'.format(self.direcao)