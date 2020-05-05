from random import randint
from car import Car
from os import getcwd
from tunnel import Tunnel
from speedline import Speedline
import pygame

def check_events():

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

def check_going(keys):
    move = None

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    if keys[pygame.K_UP]:
        move = "up"

    if keys[pygame.K_DOWN]:
        move = "down"

    return move

def check_car_turning(keys):
    move = None

    if keys[pygame.K_LEFT]:
        move = "left"

    if keys[pygame.K_RIGHT]:
        move = "right"

    return move


def imitate_speed(screen, lines, color, res, move, y):

    for line in lines.copy():
        line.ddy = 1
        if move == "up":
            line.ddy += 2
            line.rect.h += line.ddy
            line.rect.y += line.rect.h
            line.surf = pygame.transform.scale(line.surf, (1280, line.rect.h))
            line.ddy += 2

        if line.rect.y > 720:
            lines.remove(line)

def append_l(screen, lines, color, res, chord, move):
    if len(lines) < 10:
        new_line = Speedline(screen, color, res, chord)
        lines.add(new_line)

    if not move == 'up':

        for line in lines.copy():

            line.rect.h += line.ddy
            line.rect.y += (line.rect.h)

            line.surf = pygame.transform.scale(line.surf, (1280, line.rect.h))
            line.ddy += 2


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
