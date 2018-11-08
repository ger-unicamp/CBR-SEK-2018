'''
GER - UNICAMP (17/09/2018)
Autor: Natan Rodrigues

NOTE: ISTO NAO EH UMA PILHA! Foi tanto falado em pilha, pelo seu funcionamento
LIFO, mas em python decidimos criar um TAD (tipo abstrato de dados) que se encaixasse
em nossas necessidades. Btw, ISTO NAO EH UMA PILHA.

A ideia dessa classe (nome a definir) eh armazenar e processar informacoes sobre
interseccao do labirinto da competicao. Os principais metodos (push, acessa, where_to_go),
fazem isso. O push se encarrega do armazenamento, apos a validacao no codigo principal.
O metodo acessa poderia estar dentro do where_to_go, entretanto para o computador
nao faz diferenca, logo a separacao desses metodos se fez para deixar mais claro
a diferenca de cada um e quando usar. O acessa eh usado quando ja sabemos sobre todo o
labirinto, por isso o nome. Analogamente, o where_to_go, usado quando ainda nao sabemos.
'''

class Interseccao:
    def __init__(self):
        #0 DIREITA, 1 FRENTE, 2 ESQUERDA
        self.inter = {'2': -1, '3': -1, '5': -1}#as chaves sao as cores, comeca com -1 pq ainda n sabemosa  direcao
        self.verify_dir = -1#variavel para verificacao da direcao a ser 'pushed'
    def push(self, cor, direcao):
        if(self.inter['{}'.format(cor)] == -1):
            if(direcao==0):
                print('verify dir na direcao == 0: '+str(self.verify_dir))
                if self.verify_dir == -1: self.inter['{}'.format(cor)] = direcao
                else: self.inter['{}'.format(cor)]=self.verify_dir
            elif direcao == 1 and self.verify_dir == 2:
                self.inter['{}'.format(cor)] = self.verify_dir
            else:
                self.inter['{}'.format(cor)] = direcao
        self.verify_dir =-1
    def acessa(self, cor):
        return self.inter['{}'.format(cor)]
    def where_to_go(self, cor):
        if self.inter['{}'.format(cor)] != -1:
            return self.inter['{}'.format(cor)]
        else:
            if 0 not in self.inter.values():  # não tenho direita
                if 1 in self.inter.values():  #tratar o caso 1,2,0 - tenho frente
                    if self.verify_dir !=-1:  # só resta esquerda
                        self.verify_dir = 2   # confirma esquerda
                        self.inter['{}'.format(cor)] = self.verify_dir
                        return 1
                    if 2 in self.inter.values(): # tenho frente, não tenho direita e tenho esquerda
                        self.inter['{}'.format(cor)] = 0 # confirma direita
                        return 0
                self.verify_dir+=1
                return 0
            elif 1 not in self.inter.values() and self.verify_dir==-1: # tenho direita e não tenho frente e primeira tentativa
                if 2 in self.inter.values(): # já tenho direita e esquerda
                    self.inter['{}'.format(cor)] = 1 # confirma frente
                    return 1
                self.verify_dir+=1
                return 1
            else: # tenho direita - tentou frente ou tem frente
                self.verify_dir = 2
                self.inter['{}'.format(cor)] = self.verify_dir # confirma esquerda, tenho direita, já tenho ou tentei frente
                return 0
    def __str__(self):
        return '{}'.format(self.inter)
