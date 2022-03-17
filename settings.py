# Settings

import pygame


class Settings:

	def __init__(self):

		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 800

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.BLUE = (61, 183, 228)
		self.YELLOW = (253, 184, 19)
		self.ORANGE = (255, 136, 73)
		self.GREEN = (105, 190, 40)

		self.BG_COLOUR = self.BLACK

		self.ICON = pygame.image.load('images/icon.png')
		self.FONT_SIZE = 30

		self.FPS = 10

		self.INITIAL_X_VEL = 5
		self.INITIAL_Y_VEL = 0
		self.DT = 0.2

		self.massA = 10
		self.massB = 50
		self.radiusA = 10
		self.radiusB = 30
		self.colourA = self.BLUE
		self.colourB = self.ORANGE
		self.GRAV_CONST = 10

		self.TRAIL_SPACING = 15
		self.TRAIL_LENGTH = 100
		self.TRAIL_COLOUR = self.WHITE
		self.TRAIL_SIZE = 2

		