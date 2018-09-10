'''
Autor: Natan Rodrigues

A ideia da classe pilha é possibilitar o armazenamento dos dados (herança) da cor e da direção em uma interseccao. A pilha tem
caracteristica LIFO (last in first out) o que agiliza a volta do nosso robo, uma vez que a informarcao da ultima interseccao
sera a primeira a ser acessada.

Por estar em fase de testes, ainda sera feito uma descricao detalhada dos metodos aqui implementados.

Caso queira ajudar na construcao desta pilha, faca o git clone deste repo e informe sua mudanca via comentarios!
'''

from dados import Dados
class Pilha(Dados):
    def __init__(self):#no construtor, iniciamos uma lista que armazenara todos os dados a serem acessados
        self.pilha = []
    def push(self, dados):
        self.pilha.append(dados)
    def pop(self):#este metodo exclui a ultima informacao armazenada
        if(len(self.pilha)!=0):
            del(self.pilha[len(self.pilha)-1])
    def peek(self):#mostra a ultima informacao armazenada
        if(len(self.pilha)!=0):
            return self.pilha[len(self.pilha)-1]
    def acessa(self, posicao):#de tras para frente, aka, 0 -> ultimo, 1 -> penultimo...
        return self.pilha[len(self.pilha)-(posicao+1)]
    def __str__(self):#serve para dar print numa referencia dessa classe e sair de modo amigavel
        return f'{self.pilha}'
