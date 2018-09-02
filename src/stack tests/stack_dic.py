class Pilha:
    def __init__(self):
        self.pilha = {}
    def push(self, cor, direction):
        self.pilha[f'{cor}'] = direction
    def pop(self):
        if(len(self.pilha)!=0):
            # return self.pilha[len(self.pilha)-1]
            del(self.pilha.items()[len(self.pilha)-1])
    def peek(self):
        if(len(self.pilha)!=0):
            return self.pilha[len(self.pilha)-1]
    def __str__(self):
        return f'{self.pilha}'
    def tem_chave(self,chave):
        return self.pilha.has_key(f'{chave}')

pilha = Pilha()
pilha.push('vermelho', 'esq')
pilha.push(f'verde', 'dir')
pilha.push(f'amarelo', 'ret')
print(pilha)
# pilha.pop()
print(pilha)
dic = {'Natan':13, 'Jose':12}
