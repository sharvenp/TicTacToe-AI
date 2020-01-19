
from observable import Observable
from util import Utility

class TicTacToe(Observable):
	
	def __init__(self):
		Observable.__init__(self)
		self.reset_board()
	
	def reset_board(self):
		self.board = [0, 0, 0,
					  0, 0, 0,
					  0, 0, 0]
    

	def get_game_state(self):

		# Check Horizontal Win
		for i in range(3):
			index = i * 3
			if self.board[index] != 0 and \
			(self.board[index] == self.board[index + 1] == self.board[index + 2]):
				return self.board[index]

		# Check Vertical Win
		for i in range(3):
			if self.board[i] != 0 and \
			(self.board[i] == self.board[i + 3] == self.board[i + 6]):
				return self.board[i]


		# Check Diagonal Win
		if self.board[0] != 0 and \
			(self.board[0] == self.board[4] == self.board[8]):
				return self.board[0]

		if self.board[2] != 0 and \
			(self.board[2] == self.board[4] == self.board[6]):
				return self.board[2]


		if 0 in self.board:
			return 0

		return -1
	
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
			val = Utility.to_symbol(self.board[i])

			s += "| " + val + " "
			
			if (i + 1) % 3 == 0:
				s += "|"
				print(s)
				print(border)
				
				s = ""

		
