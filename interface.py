import pygame
from bezier import *


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def button(x, y, w, h, ic, ac, screen):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))


def curves(cc, c_vec, deg):
    del c_vec[:]
    for i in range(cc):
        c_i = []
        for d in range(deg + 1):
            p = Point(np.random.randint(0, 799), np.random.randint(0, 799))
            c_i.append(p)
        curve = Bezier(c_i)
        curve.color = (255, 0, 0)
        c_vec.append(curve)