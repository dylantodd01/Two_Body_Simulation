# Settings

import pygame


class Settings:

	def __init__(self):

		# BORING SETTINGS

		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1200, 800

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
		self.DT = 0.1

		self.RADIUS_A = 5
		self.colourA = self.BLUE
		self.colourB = self.YELLOW
		self.GRAV_CONST = 10000

		self.TRAIL_SPACING = 40
		self.TRAIL_LENGTH = 200
		self.TRAIL_COLOUR = self.WHITE
		self.TRAIL_SIZE = 1


		# LESS BORING SETTINGS

		# Adjust INITIAL_YA and INITIAL_YB to change the starting y coordinates of the masses
		self.INITIAL_YA = 100
		self.INITIAL_YB = 500

		# Adjust A_VEL to change the starting horizontal velocity of the smaller mass
		self.A_VEL = 12

		# Change the mass ratio to increase/decrease (massB / massA)
		self.MASS_RATIO = 10
		

		