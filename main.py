import sys
import pygame
import time

from settings import Settings
from two_bodies import TwoBodies
from display_text import Text


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

		# Set up text instructions
		self.instructions = Text(fontsize=self.settings.FONT_SIZE, position=(20, self.settings.SCREEN_HEIGHT - 30),
			message="Click anywhere to add a mass. Press space to clear the masses", colour=self.settings.WHITE)

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

#			elif event.type == pygame.MOUSEBUTTONDOWN:
#				mouse_pos = pygame.mouse.get_pos()
#				self.masses.append(MovingMass(mass=self.settings.MOVING_MASS, 
#					radius=self.mass_options[self.mass_selector.selected_mass][0], 
#					colour=self.mass_options[self.mass_selector.selected_mass][1], location=mouse_pos))
#
#			elif event.type == pygame.KEYDOWN:
#				if event.key == pygame.K_SPACE:
#					self.clear_masses()
#
#				if event.key == pygame.K_UP:
#					self.mass_selector.selector_up()
#
#				if event.key == pygame.K_DOWN:
#					self.mass_selector.selector_down()


	def update_screen(self):
		""" Update the screen """
		self.screen.fill(self.settings.BG_COLOUR)
		self.instructions.draw(self.screen)

		self.masses.draw_masses(self.screen)
		self.masses.draw_trails(self.screen)

		pygame.display.update()


simulation = TwoBodySimulation()
simulation.run()