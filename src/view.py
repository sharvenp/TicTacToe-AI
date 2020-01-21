
import pygame as pg
import time

from observer import Observer
from settings import Settings
from model import TicTacToe
from human_player import HumanPlayer
from util import Utility

class TicTacToeView(Observer):

	def __init__(self, p1, p2):

		pg.init()

		self.p1 = p1
		self.p2 = p2

		self.screen = pg.display.set_mode((Settings.WIDTH + Settings.SIDE_PANEL_WIDTH, Settings.HEIGHT))
		pg.display.set_caption("Tic Tac Toe")

	def _draw_grid(self):

		self.screen.fill((0,0,0))
		
		pg.draw.rect(self.screen, Settings.LINE_COLOR, (0, 0, Settings.WIDTH, Settings.HEIGHT), Settings.LINE_WIDTH)

		box_width = Settings.WIDTH // 3
		box_height = Settings.HEIGHT // 3

		for i in range(1, 3):
			pg.draw.line(self.screen, Settings.LINE_COLOR, (box_width*i, 0), (box_width*i, Settings.HEIGHT), Settings.LINE_WIDTH)
			pg.draw.line(self.screen, Settings.LINE_COLOR, (0, box_height*i), (Settings.WIDTH, box_height*i), Settings.LINE_WIDTH)


		self._render_side_panel()

		pg.display.update()

	def _render_screen(self, o):

		font = pg.font.SysFont(Settings.BOARD_FONT[0], Settings.BOARD_FONT[1])

		box_width = Settings.WIDTH // 3
		box_height = Settings.HEIGHT // 3

		for i in range(len(o.board)):

			if o.board[i] != 0:

				x = i % 3
				y = i // 3

				symbol = Utility.to_symbol(o.board[i])

				color = Settings.X_COLOR

				if symbol == "O":
					color = Settings.O_COLOR

				font_surface = font.render(symbol, True, color)
				font_rect = font_surface.get_rect(center=((x * box_width) + (box_width // 2), (y * box_height) + (box_height // 2)))
				self.screen.blit(font_surface, font_rect)

		pg.display.update()

	def _render_side_panel(self):

		font = pg.font.SysFont(Settings.PANEL_FONT[0], Settings.PANEL_FONT[1])

		p1_surface = font.render(f"X: {self.p1.score}", True, Settings.X_COLOR)
		self.screen.blit(p1_surface, (Settings.WIDTH + 30, 50, 100, 100))

		p1_surface = font.render(f"O: {self.p2.score}", True, Settings.O_COLOR)
		self.screen.blit(p1_surface, (Settings.WIDTH + 30, 50 + Settings.PANEL_FONT[1], 100, 100))


	def update(self, o):
		
		Utility.print(f"Notified by {o}")
		
		self.turn_counter += 1
		game_state = o.get_game_state()
		self._render_screen(o);

		# Reset board
		if game_state != 0:
			
			self.game_over = True

			if game_state == 1:
				self.p1.add_win_point()

			elif game_state == 2:
				self.p2.add_win_point()

			else:
				self.p1.add_draw_point()
				self.p2.add_draw_point()

			
			
			if game_state != -1:
				Utility.print(f"{Utility.to_symbol(game_state)} Wins!")
			else:
				Utility.print("Draw!")


			Utility.print(f"X: {self.p1.score}   O: {self.p2.score}")

			time.sleep(1)

			o.reset_board()
			self._draw_grid()
			self._render_side_panel()

	def launch(self):

		alternator = 0
		self._draw_grid()

		while True:

			self.turn_counter = alternator
			self.game_over = False

			pg.event.clear()

			while not self.game_over:

				e = pg.event.poll()
				if e.type == pg.QUIT: 
					quit(0)

				if self.turn_counter % 2 == 0:
					if type(self.p1) == HumanPlayer:
						self.p1.move(e)
					else:
						self.p1.move()
				else:
					if type(self.p2) == HumanPlayer:
						self.p2.move(e)
					else:
						self.p2.move()


			alternator = (alternator + 1) % 2
