# Settings

import pygame


class Settings:

	def __init__(self):

		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1400, 900

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.BLUE = (61, 183, 228)
		self.YELLOW = (253, 184, 19)
		self.ORANGE = (255, 136, 73)
		self.GREEN = (105, 190, 40)

		self.BG_COLOUR = self.BLACK

		self.ICON = pygame.image.load('images/icon.png')
		self.FONT_SIZE = 30

		self.FPS = 10000

		self.INITIAL_A_COORDS = (500, 400)
		self.INITIAL_B_COORDS = (700, 600)
		self.INITIAL_X_VEL_A = 8
		self.INITIAL_X_VEL_B = -4
		self.DT = 0.1

		self.massA = 1
		self.massB = 2
		self.radiusA = 10
		self.radiusB = 15
		self.colourA = self.BLUE
		self.colourB = self.ORANGE
		self.GRAV_CONST = 10000

		self.TRAIL_SPACING = 40
		self.TRAIL_LENGTH = 200
		self.TRAIL_COLOUR = self.WHITE
		self.TRAIL_SIZE = 1

		