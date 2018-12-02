import sys
import pygame
import numpy as np
from bezier import *

args = len(sys.argv)
if args == 1:
	print("Configuração Padrão:\n\
	Grau: 3\n\
	Curvas: 5")
	deg = 3
	cc = 5
elif args == 2:
	print("Configuração:\n\
	Grau: 3\n\
	Curvas: %s" %  sys.argv[1])
	deg = 3
	cc = int(sys.argv[1])
else:
	print("Configuração:\n\
	Grau: %s\n\
	Curvas: %s" %  (sys.argv[2], sys.argv[1]))
	deg = int(sys.argv[2])
	cc = int(sys.argv[1])


pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size = [800, 800]
purple = (255, 0, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("EP1 - MAC 0210")

clock = pygame.time.Clock()
done = False


c = [black, red, green, blue, purple]
c_vec = []

for i in range(cc):
	c_i = []
	for d in range(deg + 1):
		p = Point(np.random.randint(0,799), np.random.randint(0,799))
		c_i.append(p)
	curve = Bezier(c_i)
	curve.color = red
	c_vec.append(curve)



while not done:
	clock.tick(10)
	mousepos = (0, 0)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			for bez in c_vec:
				bez.color = red
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
