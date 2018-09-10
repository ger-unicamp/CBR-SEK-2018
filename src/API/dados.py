class Dados:
	def __init__(self):  # variavéis que podem ser do tipo inteiro
		self.dir = 0
		self.cor = 0

	# métodos set(aterar) e set (consultar)
	def setDir(self,dir):
		self.dir = dir

	def setCor(self, cor):
		self.cor=cor

	def getDir(self):
		return self.dir

	def getCor(self):
		return self.cor

	def __str__(self):
		pass
