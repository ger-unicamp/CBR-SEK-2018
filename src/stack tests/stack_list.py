class Pilha:
    def __init__(self):
        self.pilha = []
    def push(self, direction):
        self.pilha.append(direction)
    def pop(self):
        if(len(self.pilha)!=0):
            # return self.pilha[len(self.pilha)-1]
            del(self.pilha[len(self.pilha)-1])
    def peek(self):
        if(len(self.pilha)!=0):
            return self.pilha[len(self.pilha)-1]
    def __str__(self):
        return f'{self.pilha}'

pilha = Pilha()
pilha.push("dir")
pilha.push("esq")
pilha.push("r")
pilha.push("esq")
print(pilha)
pilha.pop()
print(pilha.peek())
print(pilha)
