from random import randint
from car import Car
from os import getcwd
from tunnel import Tunnel
from speedline import Speedline
import pygame


def check_events():

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def check_going(keys):

    if keys[pygame.K_UP]:
        return "up"

    if keys[pygame.K_DOWN]:
        return "down"

def check_car_turning(keys, car):

    if keys[pygame.K_LEFT]:
        car.car_move("left")

    elif keys[pygame.K_RIGHT]:
        car.car_move("right")

    else:
        car.car_move(None)


def imitate_speed(lines, move):

    if move == "up":
        for line in lines:
            line.rect.y += (line.rect.y // (lines.index(line)*10+1))


def append_l(screen, lines, color, res, chord, move):

    if len(lines) < 15:
        for i in range(15):
            newline = Speedline(screen, color, res, chord-20, i*5+1)
            lines.append(newline)
            chord += 10*(i+1)

    [lines.remove(line) for line in lines.copy() if line.rect.y > 1280]

def append_bots(cars, screen, x):
    if len(cars) < 2:
        new_car = Car(screen)
        new_car.rect.y = 470
        new_car.rect.x = randint(x-new_car.rect.w, x+new_car.rect.w)
        new_car.image = pygame.transform.scale(pygame.image.load(getcwd()+"\\images\\nissan2.png").convert_alpha(), new_car.scal)

        cars.add(new_car)

def bot_moving(cars):

    for bot in cars:
        bot.rect.y += 2
        bot.scal[0] += 3
        bot.scal[1] += 2
        bot.image = pygame.transform.scale(pygame.image.load(getcwd()+"\\images\\nissan2.png").convert_alpha(), bot.scal)

        if bot.rect.y > 720:
            cars.remove(bot)

def append_tun(tunnels, screen, x):
    if len(tunnels) < 1:
        new_tunnel = Tunnel(screen)
        new_tunnel.rect_t_l.y, new_tunnel.rect_t_r.y = 430, 430
        new_tunnel.rect_t_l.x, new_tunnel.rect_t_r.x = 620, 660-new_tunnel.rect_t_r.w

        tunnels.add(new_tunnel)

def tunnel_mov(tunnels):

    for elem in tunnels:
        elem.rect_t_l.y -= 6
        elem.rect_t_r.y -= 6

        elem.rect_t_l.x -= 45
        elem.rect_t_r.x += 5

        elem.scal[0] += 50
        elem.scal[1] += 7
        elem.tunnel_l = pygame.transform.scale(pygame.image.load(getcwd()+"\\images\\tunnel_a.png").convert_alpha(), elem.scal)
        elem.tunnel_r = pygame.transform.scale(pygame.image.load(getcwd()+"\\images\\tunnel_b.png").convert_alpha(), elem.scal)

        if elem.rect_t_r.y < -12:
            tunnels.remove(elem)
