
class Utility:
	@staticmethod
	def to_symbol(value):
		if value == 1:
			return "X"
		elif value == 2:
			return "O"
		else:
			return " "