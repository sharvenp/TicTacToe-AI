
import pygame as pg

from player import Player

class HumanPlayer(Player):

	def __init__(self):
		Player.__init__(self)

	def move(self):
		
		