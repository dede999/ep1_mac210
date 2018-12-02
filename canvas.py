import pygame
import numpy as np
from bezier import *

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size = [800, 800]
purple = (255, 0, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("EP1")

clock = pygame.time.Clock()
done = False


c = [black, red, green, blue, purple]
c_vec = []

for i in range(5):
	p0 = Point(np.random.randint(0,799), np.random.randint(0,799))
	p1 = Point(np.random.randint(0,799), np.random.randint(0,799))
	p2 = Point(np.random.randint(0,799), np.random.randint(0,799))
	c_i = [p0, p1, p2]
	curve = Bezier(c_i)
	curve.color = red
	c_vec.append(curve)



while not done:
	clock.tick(10)
	mousepos = (0, 0)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mousepos = pygame.mouse.get_pos()
			clique = Point(mousepos[0], mousepos[1])
			closest(clique, c_vec)
		if event.type == pygame.QUIT:
			done = True
	screen.fill(white)
	for c in c_vec:
		# list_pts = []
		for i in range(len(c.x_pts) - 1):
			# list_pts.append([c.x_pts[i], c.y_pts[i]])
			pygame.draw.line(screen, c.color, [int(c.x_pts[i]), int(c.y_pts[i])],
			                 [int(c.x_pts[i + 1]), int(c.y_pts[i + 1])], 1)
	pygame.display.flip()

pygame.quit()
