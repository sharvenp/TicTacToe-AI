
class Player:
	
	def __init__(self, model, value):
		self.score = 0
		self.model = model
		self.value = value

	def move(self):
		raise NotImplementedError