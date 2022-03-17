import pygame
import numpy as np

from settings import Settings
from step_runge_kutta import RungeKuttaMethod

class TwoBodies:

	def __init__(self):
		self.settings = Settings()
		self.RK4 = RungeKuttaMethod()

		self.massA = self.settings.massA
		self.radiusA = self.settings.radiusA
		self.massB = self.settings.massB
		self.radiusB = self.settings.radiusB
		self.colourA = self.settings.colourA
		self.colourB = self.settings.colourB

		self.dt = self.settings.DT

		self.trailA = []
		self.trailB = []
		self.trail_iterations = 0

		self.z_vec = np.array([700, 0, 300, 0, 500, 0, 500, 0]) # Vector of form [xa, xa', ya, ya', xb, xb', yb, yb']



	def update_masses(self):
		self.z_vec = self.RK4.step(self.z_vec, self.massA, self.massB, self.dt)
		self.locationA = (self.z_vec[0], self.z_vec[2])
		self.locationB = (self.z_vec[4], self.z_vec[6])


	def draw_masses(self, screen):
		pygame.draw.circle(screen, self.colourA, self.locationA, self.radiusA)
		pygame.draw.circle(screen, self.colourB, self.locationB, self.radiusB)


	def draw_trails(self, screen):
		for i, location in enumerate(self.trailA):
			pygame.draw.circle(screen, self.settings.TRAIL_COLOUR, location, self.settings.TRAIL_SIZE)
			pygame.draw.circle(screen, self.settings.TRAIL_COLOUR, self.trailB[i], self.settings.TRAIL_SIZE)


	def update_trails(self):
		
		if (self.trail_iterations % self.settings.TRAIL_SPACING) != 0:
			self.trail_iterations += 1
			return

		if len(self.trailA) < self.settings.TRAIL_LENGTH:
			self.trailA.append(self.locationA)
		else:
			self.trailA.pop(0)
			self.trailA.append(self.locationA)

		if len(self.trailB) < self.settings.TRAIL_LENGTH:
			self.trailB.append(self.locationB)
		else:
			self.trailB.pop(0)
			self.trailB.append(self.locationB)
		
		self.trail_iterations += 1






