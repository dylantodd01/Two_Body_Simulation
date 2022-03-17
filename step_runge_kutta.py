import math
import numpy as np

from settings import Settings

class RungeKuttaMethod:

	def __init__(self):
		self.settings = Settings()

	def state_deriv(self, z, massA, massB):
		r_x = (z[0] - z[4])
		r_y = (z[1] - z[5])

		if r_x == 0:
			r_x = 0.001

		R = math.sqrt((r_x ** 2) + (r_y ** 2))

		sign_x = 1 if r_x < 0 else -1
		sign_y = 1 if r_y < 0 else -1

		theta = math.atan(r_y / r_x)

		force = self.settings.GRAV_CONST * ((massA * massB) / (R**2 + 0.1))
		forceA_x = force * abs(math.cos(theta)) * sign_x
		forceA_y = force * abs(math.sin(theta)) * sign_y
		forceB_x = -1 * forceA_x
		forceB_y = -1 * forceA_y
		print(f"\nFORCE ON A: Fx = {forceA_x}, Fy = {forceA_y} \nFORCE ON B: Fx = {forceB_x}, Fy = {forceB_y}")

		z1 = z[1]
		z2 = forceA_x / massA
		z3 = z[3]
		z4 = forceA_y / massA
		z5 = z[5]
		z6 = forceB_x / massB
		z7 = z[7]
		z8 = forceB_y / massB

		return np.array([z1, z2, z3, z4, z5, z6, z7, z8])

	def step(self, z_vec, massA, massB, dt):
		A = dt * self.state_deriv(z_vec, massA, massB)
		B = dt * self.state_deriv(z_vec + A/2, massA, massB)
		C = dt * self.state_deriv(z_vec + B/2, massA, massB)
		D = dt * self.state_deriv(z_vec + C, massA, massB)

		return (z_vec + (1 / 6) * (A + 2 * B + 2 * C + D))

