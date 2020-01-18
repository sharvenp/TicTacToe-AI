
import pygame as pg

from observer import Observer
from settings import Settings
from model import TicTacToe
from human_player import HumanPlayer

class TicTacToeView(Observer):

	def __init__(self, p1, p2):

		pg.init()

		self.p1 = p1
		self.p2 = p2

		self.screen = pg.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
		pg.display.set_caption("Tic Tac Toe")

	def _draw_grid(self):
		
		pg.draw.rect(self.screen, Settings.LINE_COLOR, (0, 0, Settings.WIDTH, Settings.HEIGHT), Settings.LINE_WIDTH)

		box_width = Settings.WIDTH // 3
		box_height = Settings.HEIGHT // 3

		for i in range(1, 3):
			pg.draw.line(self.screen, Settings.LINE_COLOR, (box_width*i, 0), (box_width*i, Settings.HEIGHT), Settings.LINE_WIDTH)
			pg.draw.line(self.screen, Settings.LINE_COLOR, (0, box_height*i), (Settings.WIDTH, box_height*i), Settings.LINE_WIDTH)

		pg.display.update()

	def _render_screen(self, o):

		font = pg.font.SysFont(Settings.FONT[0], Settings.FONT[1])

		box_width = Settings.WIDTH // 3
		box_height = Settings.HEIGHT // 3

		for i in range(len(o.board)):

			if o.board[i] != 0:

				x = i % 3
				y = i // 3

				symbol = " "

				if o.board[i] == 1:
					symbol = "X"
				elif o.board[i] == 2:
					symbol = "O"

				font_surface = font.render(symbol, True, Settings.FONT_COLOR)
				font_rect = font_surface.get_rect(center=((x * box_width) + (box_width // 2), (y * box_height) + (box_height // 2)))
				self.screen.blit(font_surface, font_rect)

		pg.display.update()

	def update(self, o):
		print(f"Notified by {o}")
		self.game_over = bool(o.get_game_state)
		self._render_screen(o);

	def launch(self):

		alternator = 0
		self._draw_grid()

		while True:

			turn_counter = alternator
			self.game_over = False

			while not self.game_over:

				e = pg.event.poll()
				if e.type == pg.QUIT: 
					quit(0)

				if turn_counter % 2 == 0:
					if type(self.p1) == HumanPlayer:
						self.p1.move(e)
					else:
						self.p1.move()
				else:
					if type(self.p2) == HumanPlayer:
						self.p2.move(e)
					else:
						self.p2.move()


			alternator += 1
			alternator %= 2

			# Update Winner


