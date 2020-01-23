from tree import Tree
from speedline import Speedline
import pygame

def check_events():

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())



def check_keydown_events(keys):
    move = None

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    if keys[pygame.K_LEFT]:
        move = "left"

    if keys[pygame.K_RIGHT]:
        move = "right"

    if keys[pygame.K_UP]:
        move = "up"

    if keys[pygame.K_DOWN]:
        move = "down"

    return move


def imitate_speed(screen, lines, color, res, move, y):

    for line in lines.copy():

        if move == "up":
            line.rect.y += 50

        line.rect.h += line.ddy*2
        line.rect.y += (line.rect.h)/2
        line.ddy += 1


        if line.rect.y > 720:
            line.rect.y = y
            line.ddy = 1
            line.rect.h = 0


def append_l(screen, lines, color, res, chord, move):
    if len(lines) < 18:
        new_line = Speedline(screen, color, res, chord)
        lines.add(new_line)

def append_tr(screen, trees, bottom, x):
    if len(trees) < 10:
        new_tree = Tree(screen, bottom, x)
        trees.add(new_tree)

def move_tr(screen, trees, move):

    for tr in trees.copy():

        if move == "down":
            break


        tr.rect_l.y += tr.rect_im.h/6
        tr.rect_l.x -= (tr.rect_im.w/2 + 30)

        tr.rect_l2.y += tr.rect_im.h/6
        tr.rect_l2.x = (1280 - tr.rect_l.x - tr.rect_l.w)

        tr.sec_rect_im.y += tr.rect_im.h/6
        tr.rect_im.y += tr.rect_im.h/6

        tr.rect_im.x -= (tr.rect_im.w/2 + 25)
        tr.sec_rect_im.x = (1280 - tr.rect_im.x - tr.rect_im.w)


        if tr.rect_im.y >= 720:
            trees.remove(tr)


def make_map(i):

    world = [False, False, True, True, False, False]

    return world[i]
