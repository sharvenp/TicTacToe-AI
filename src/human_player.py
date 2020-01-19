
import pygame as pg

from player import Player
from settings import Settings

class HumanPlayer(Player):

	def __init__(self, model, value):
		Player.__init__(self, model, value)


	def move(self, e):
		
		if e.type == pg.MOUSEBUTTONDOWN:

			mx, my = pg.mouse.get_pos()

			if not (0 <= mx <= Settings.WIDTH and 0 <= my <= Settings.HEIGHT):
				return
				
			x = (mx*3) // Settings.WIDTH 
			y = (my*3) // Settings.HEIGHT

			index = x + 3*y

			response = self.model.play_move(index, self.value)
			print(response)