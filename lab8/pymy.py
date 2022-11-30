import pygame
from pygame.draw import *
from random import randint
from numpy import sign

pygame.init()
wide = 1200
vicota = 600
FPS = 50
screen = pygame.display.set_mode((wide, vicota))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, BLACK, GREEN, MAGENTA, CYAN]

shyot = 0
balls = []
zloy = []

def new_ball(lict):
    '''
    ricyet sharik
    x, y - coordinati centra
    r - radius sharika
    color - cvet sharika
    '''
    global x, y, r
    maxr = 50
    x = randint(3 * maxr, wide - 3 * maxr)
    y = randint(3 * maxr, vicota - 3 * maxr)
    r = randint(30, maxr)
    vx = 0.003 * randint(-30, 30)
    vy = 0.003 * randint(-30, 30)
    color = COLORS[randint(0, 5)]
    lict.append((color, (x, y), r, vx, vy))
    return lict


for i in range(8):
    maxr = 50
    balls.append(tuple((COLORS[randint(0, 5)],
                        (randint(3 * maxr, wide - 3 * maxr), randint(3 * maxr, vicota - 3 * maxr)), randint(30, 50),
                        0.003 * randint(-30, 30), 0.003 * randint(-30, 30))))


def newnew_ball(lict):
    for i in range(len(lict)):
        circle(screen, lict[i][0], lict[i][1], lict[i][2], )


def click(event, kunteynir, lict):
    '''
    opredelyaet popadanie clicka v sharik
    event.pos - coordinati clicka
    s_1 - rasstoyanie ot centra sharika do mesta clicka
    kunteynir - kolichestvo popadaniy
    '''
    papal = 0
    x = zloy[0][1][0]
    y = zloy[0][1][1]
    r = zloy[0][0]
    ro = ((event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2) ** 0.5
    if ro > r:
        print('mimo covershenno')
    else:
        papal += 1
        print('pryamoe popadanie')
    for ball in lict:
        x_i = ball[1][0]
        y_i = ball[1][1]
        r_i = ball[2]
        s_1 = ((event.pos[0] - x_i) ** 2 + (event.pos[1] - y_i) ** 2) ** 0.5
        if s_1 <= r_i:
            papal = 1
            kunteynir += 1
            lict.remove(ball)
            lict = new_ball(lict)
    if papal == 0:
        print('mimo, schet ', kunteynir)
    else:
        print('papal, schet ', kunteynir)

    return kunteynir, lict


def mishen(zloy):
    x = randint(100, wide - 100)
    y = randint(100, vicota - 100)
    r = 100
    circle(screen, (255, 255, 0), (x, y), r)
    circle(screen, (0, 0, 0), (x, y), r, 5)
    rect(screen, (0, 0, 0), (x - 50, y + 25, 100, 25))
    circle(screen, (255, 0, 0), (x - 50, y - 25), 20)
    circle(screen, (0, 0, 0), (x - 50, y - 25), 20, 1)
    circle(screen, (255, 0, 0), (x + 50, y - 15), 15)
    circle(screen, (0, 0, 0), (x + 50, y - 15), 15, 1)
    circle(screen, (0, 0, 0), (x - 50, y - 25), 10)
    circle(screen, (0, 0, 0), (x + 50, y - 15), 7)
    pygame.draw.line(screen, BLACK,
                     [x - 70, y - 50],
                     [x - 30, y - 50], 7)
    pygame.draw.line(screen, BLACK,
                     [x + 70, y - 50],
                     [x + 30, y - 40], 7)
    zloy.append((r, (x, y)))

    return zloy


def dvig(lict, dt):
    for i in range(len(lict)):
        ball = lict[i]
        lict[i] = (ball[0], (ball[1][0] + ball[3] / dt, ball[1][1] + ball[4] / dt), ball[2], ball[3], ball[4])
        if (ball[1][0]) >= (wide - ball[2]) or (ball[1][0] <= ball[2]):
            lict[i] = (ball[0], (ball[1][0] - sign(ball[3]) * 15, ball[1][1]), ball[2], -ball[3], ball[4])

        if (ball[1][1]) >= (vicota - ball[2]) or (ball[1][1] <= ball[2]):
            lict[i] = (ball[0], (ball[1][0], ball[1][1] - sign(ball[4]) * 15), ball[2], ball[3], -ball[4])

    return lict


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shyot, balls = click(event, shyot, balls)
    # new_ball()
    mishen(zloy)
    newnew_ball(balls)
    balls = dvig(balls, 1 / FPS)
    pygame.display.update()
    screen.fill((254, 255, 255))

pygame.quit()
