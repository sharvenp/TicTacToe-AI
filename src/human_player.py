
import pygame as pg

from player import Player

class HumanPlayer(Player):

	def __init__(self, model):
		Player.__init__(self, model)


	def move(self):
		
		e = pg.event.poll()

		if e.type == pg.MOUSEBUTTONDOWN:

			print("Click")