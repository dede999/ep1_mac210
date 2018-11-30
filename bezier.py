import pygame
import numpy as np
import scipy.special as sci


class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def dist(self, other):
		return np.sqrt(np.power((self.x - other.x), 2) + np.power((self.y - other.y), 2))


class Bezier:

	def __init__(self, points):
		self.x_cord = []
		self.y_cord = []
		for p in points:
			self.x_cord.append(p.x)
			self.y_cord.append(p.y)
		self.degree = len(points) - 1
		self.x_eq = []
		self.y_eq = []
		self.x_max = np.infty * -1
		self.y_max = np.infty * -1
		self.x_min = np.infty
		self.y_min = np.infty
		self.x_pts = []
		self.y_pts = []
		if len(points) > 1:
			self.make_equation()
			self.get_values()

	def make_equation(self):
		d = self.degree
		x, y = [], []
		[x.append(a) for a in self.x_cord.__reversed__()]
		[y.append(a) for a in self.y_cord.__reversed__()]
		offset = 0
		while d >= 0:
			newton = []
			for k in range(d + 1):
				newton.append(sci.comb(d, k, exact=True) * np.power(-1, k))
			self.x_eq.append(int(
				np.matmul(np.array(newton), np.array(x[offset:len(x)])) * sci.comb(self.degree, offset, exact=True)))
			self.y_eq.append(int(
				np.matmul(np.array(newton), np.array(y[offset:len(y)])) * sci.comb(self.degree, offset, exact=True)))
			d -= 1
			offset += 1

	def get_values(self):
		t = 0.0
		# esse é o valor de incremento, podemos alterar em outros momento
		delta = 0.05
		while t <= 1:
			x = np.polyval(self.x_eq, t)
			y = np.polyval(self.y_eq, t)
			if x > self.x_max:
				self.x_max = x
			elif x < self.x_min:
				self.x_min
			if y > self.y_max:
				self.y_max = y
			elif y < self.y_min:
				self.y_min
			self.x_pts.append(x)
			self.y_pts.append(y)
			t += delta


def closest(point, bezier):
	close = None
	distance = np.infty
	for curve in bezier:
		der_x = np.polyder(curve.x_eq)
		der_y = np.polyder(curve.y_eq)
		x = 2 * curve.x_eq
		y = 2 * curve.y_eq
		x[-1] -= 2 * point.x
		y[-1] -= 2 * point.y
		d_f = np.polyadd(np.polymul(x, der_x), np.polymul(y, der_y))
		for r in np.roots(d_f):
			if np.isreal(r) and r <= 1 and r >= 0:
				p = Point(np.polyval(curve.x_eq, r), np.polyval(curve.y_eq, r))
				d = p.dist(point)
				if d < distance:
					close = p
					distance = d
	return close


a = Point(0, 8)
b = Point(1, 7)
c = Point(4, 5)
d = Point(3, 2)
pontos = [a, b, c, d]
curve = Bezier(pontos)
print(curve.x_eq)
print(curve.y_eq)
