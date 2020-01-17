
class Player:
	
	def __init__(self, model):
		self.score = 0
		self.model = model

	def move(self):
		raise NotImplementedError