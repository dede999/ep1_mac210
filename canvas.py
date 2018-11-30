import pygame
import bezier

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
