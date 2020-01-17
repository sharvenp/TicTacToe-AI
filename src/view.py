
import pygame as pg

from observer import Observer
from settings import Settings
from model import Model

class TicTacToeView(Observer):

	def __init__(self, p1, p2):

		pg.init()

		self.screen = pg.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
		pg.display.set_caption("Tic Tac Toe")

	def _render_screen(self, o):

		pg.display.update()

	def update(self, o):
		print(f"Notified by {o}")
		self.game_over = bool(o.get_game_state)
		self._render_screen(o);

	def launch(self):

		alternator = 0

		while True:

			turn_counter = alternator
			self.game_over = False

			while not game_over:

				if turn_counter % 2 == 0:
					self.p1.move()
				else:
					self.p2.move()


			alternator += 1
			alternator %= 2

			# Update Winner


