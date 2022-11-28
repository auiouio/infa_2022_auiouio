import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

circle(screen, (255,255,0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 5)
rect(screen, (0, 0, 0), (150, 200, 100, 25))
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (0, 0, 0), (150, 150), 20, 1)
circle(screen, (255, 0, 0), (250, 160), 15)
circle(screen, (0, 0, 0), (250, 160), 15, 1)
circle(screen, (0, 0, 0), (150, 150), 10)
circle(screen, (0, 0, 0), (250, 160), 7)
pygame.draw.line(screen, BLACK,
                 [130, 115],
                 [170, 125], 7)
pygame.draw.line(screen, BLACK,
                 [270, 125],
                 [230, 135], 7)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()