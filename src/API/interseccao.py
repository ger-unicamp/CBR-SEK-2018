'''
Autor: Natan Rodrigues

A ideia da classe pilha é possibilitar o armazenamento dos dados (herança) da cor e da direção em uma interseccao. A pilha tem
caracteristica LIFO (last in first out) o que agiliza a volta do nosso robo, uma vez que a informarcao da ultima interseccao
sera a primeira a ser acessada.

Por estar em fase de testes, ainda sera feito uma descricao detalhada dos metodos aqui implementados.

Caso queira ajudar na construcao desta pilha, faca o git clone deste repo e informe sua mudanca via comentarios!
'''

class Interseccao:
    def __init__(self):
        self.pilha = {'red': 0, 'green': 0, 'blue': 0}
    def push(self, cor, direcao):
        self.pilha[f'{cor}'] = direcao
    def acessa(self, cor):
        return self.pilha[f'{cor}']
    def __str__(self):
        return f'{self.pilha}'
