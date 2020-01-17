
from observable import Observable

class TicTacToe(Observable):
	
	def __init__(self):

		self.board = [0, 0, 0,
					  0, 0, 0,
					  0, 0, 0]
    
    def get_game_state(self):
    	if 0 in self.board:
    		return 0

    	return 1

	def play_move(self, index, value):

		if 0 <= index <= 8:
			if self.board[index] == 0:
				self.board[index] = value
				self.notify_observers()
				return f"Placed {value} @ index {index}"
			else:
				return f"Square Occupied. Value: {self.board[index]}"
		else:
			return f"Index Out of Bounds: {index}"


	def print_board(self):
		"""
		prints:
		+-----------+
		| 0 | 1 | 2 |
		+-----------+
		| 3 | 4 | 5 |
		+-----------+
		| 6 | 7 | 8 |
		+-----------+
		"""

		border = "+-----------+" 
		s = ""
		print(border)
		for i in range(len(self.board)):
			val = " "
			
			if self.board[i] == 1:
				val = "X"
			elif self.board[i] == 2:
				val = "O"

			s += "| " + val + " "
			
			if (i + 1) % 3 == 0:
				s += "|"
				print(s)
				print(border)
				
				s = ""

		
