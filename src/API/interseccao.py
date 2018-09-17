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

Por estar em fase de testes, ainda sera feito uma descricao detalhada dos metodos aqui implementados.

Caso queira ajudar na construcao desta pilha, faca o git clone deste repo e informe sua mudanca via comentarios!
'''

class Interseccao:
    def __init__(self):# construtor
        self.inter = {'2': -1, '3': -1, '5': -1}#as chaves sao as cores, comeca com -1 pq ainda n sabemosa  direcao
    def push(self, cor, direcao):
        self.inter[f'{cor}'] = direcao
    def acessa(self, cor):
        return self.inter[f'{cor}']
	def where_to_go(self, cor):
		if self.iter[f'{cor}'] != -1:
			return self.iter[f'{cor}']
		else:
			if 0 not in self.inter.values():
				return 0
			elif 1 not in self.inter.values():
				return 1
			elif 2 not in self.inter.values():
				return 2
    def __str__(self):#metodo para dar print
        return f'{self.inter}'
