from dados import Dados
class Pilha(Dados):
    def __init__(self):
        self.pilha = []
    def push(self, dados):
        self.pilha.append(dados)
    def pop(self):
        if(len(self.pilha)!=0):
            # return self.pilha[len(self.pilha)-1]
            del(self.pilha[len(self.pilha)-1])
    def peek(self):
        if(len(self.pilha)!=0):
            return self.pilha[len(self.pilha)-1]
    def __str__(self):
        return f'{self.pilha}'
