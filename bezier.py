import pygame
# import numpy as np
# import scipy.special as sci
#
#
#
# class Point:
#
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# class Bezier:
#
# 	def __init__(self, points):
# 		self.x_cord = []
# 		self.y_cord = []
# 		for p in points:
# 			self.x_cord.append(p.x)
# 			self.y_cord.append(p.y)
# 		self.degree = len(points) - 1
# 		self.x_eq = []
# 		self.y_eq = []
# 		self.x_max = np.infty * -1
# 		self.y_max = np.infty * -1
# 		self.x_min = np.infty
# 		self.y_min = np.infty
# 		# if points.length > 1:
#
# 	def make_equation(self):
# 		d = self.degree
# 		x, y = [], []
# 		[x.append(a) for a in self.x_cord.__reversed__()]
# 		[y.append(a) for a in self.y_cord.__reversed__()]
# 		offset = 0
# 		while d >= 0:
# 			newton = []
# 			for k in range(d+1):
# 				newton.append(sci.comb(d,k, exact=True) * np.power(-1, k))
# 			self.x_eq.append(int(np.matmul(np.array(newton), np.array(x[offset:len(x)]))*sci.comb(self.degree,offset,exact=True)))
# 			self.y_eq.append(int(np.matmul(np.array(newton), np.array(y[offset:len(y)]))*sci.comb(self.degree,offset,exact=True)))
# 			d -= 1
# 			offset += 1

	# def get_values(self):
	# 	t =
#
# a = Point(0, 8)
# b = Point(1, 7)
# c = Point(4, 5)
# d = Point(3, 2)
# pontos = [a, b, c, d]
# curve = Bezier(pontos)
# curve.make_equation()
# print(curve.x_eq)
# print(curve.y_eq)
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("EP1")

clock = pygame.time.Clock()
done = False

while not done:
	clock.tick()
	screen.fill(white)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mousepos = pygame.mouse.get_pos()
			print(mousepos)
		if event.type == pygame.QUIT:
			done = True

pygame.quit()
