import sys
import pygame
import time

from settings import Settings
from two_bodies import TwoBodies

class TwoBodySimulation:

	def __init__(self):
		# Initialise pygame
		pygame.init()

		# Initialise the pygame settings
		self.settings = Settings()

		# Set up window
		self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
		pygame.display.set_caption("2 Body Simulation")
		pygame.display.set_icon(self.settings.ICON)

		# Initialise the mass bodies
		self.masses = TwoBodies()
		

	def run(self):
		""" Main loop """
		while True:
			self.check_events()

			self.masses.update_masses()
			self.masses.update_trails()

			self.update_screen()
			time.sleep(1/self.settings.FPS)


	def check_events(self):
		""" Check for user input events """
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				sys.exit()

	def update_screen(self):
		""" Update the screen """
		self.screen.fill(self.settings.BG_COLOUR)

		self.masses.draw_masses(self.screen)
		self.masses.draw_trails(self.screen)

		pygame.display.update()


simulation = TwoBodySimulation()
simulation.run()