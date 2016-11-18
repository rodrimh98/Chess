import table as tab

T = tab.table()

class peon(object):
	valor = 1
	pos = [0,0]
	influence_pos = []
	name = 'peon'
	score = 0
	temp_pos = []

	def posible_move(self):
		temp = []
		temp2 = []
		temp = [self.pos[0] + 1 , self.pos[1]] #El valor que debe aumentar en el movimiento del peon debe ser el valor i (eje x) para que cambie de fila a una superior
		self.temp_pos=[]
		for i in range(len(temp)):
			if (temp[i]>=0 and temp[i]<=7):
				temp2.append(temp[i])

		self.temp_pos = temp2
		

	def temp_influence (self):
		temp = []
		temp = [[self.temp_pos[0]+1,self.temp_pos[1]+1],[self.temp_pos[0]+1,self.temp_pos[1]-1]]
		self.influence_pos = []
		for i in range(len(temp)):
			j=0
			if (temp[i][j]>=0 and temp[i][j]<=7 and temp[i][j+1]>=0 and temp[i][j]<=7):
				self.influence_pos.append(temp[i])


	def score (self):
		self.score = 0
		for i in range((len(self.influence_pos))):
			j = 0
			self.score = self.valor * T[self.influence_pos][i].value + self.score
			self.score = self.score + self.valor*T[self.pos].value
		#	T[self.influence_pos[i][0],self.influence_pos[i][1]].influencia = score
					
	def move(slef):
		self.pos = self.temp_pos



