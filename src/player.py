
class Player:
	
	def __init__(self, model, value):
		self.score = 0.0
		self.model = model
		self.value = value

	def add_win_point(self):
		self.score += 1.0

	def add_draw_point(self):
		self.score += 0.5

	def move(self):
		raise NotImplementedError