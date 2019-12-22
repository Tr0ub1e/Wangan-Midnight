from tree import Tree
from speedline import Speedline
import pygame

def check_events(turn, TURNING):

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == TURNING:
            if turn == 'left':

                turn = 'center'
                break

            if turn == 'center':

                turn = 'right'
                break

            if turn == 'right':

                turn = 'left'
                break

    return turn


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


def imitate_speed(screen, lines, color, res, move):

    for line in lines.copy():

        if move == "down":
            break

        line.rect.height += 720/line.rect.y
        line.rect.y += 4

        if line.rect.y >= 720:
            lines.remove(line)


    if not move == "up":
        for line in lines.copy():
            line.rect.y += 100


def append_l(screen, lines, color, res, move):
    if len(lines) < 5:
        new_line = Speedline(screen, color, res)
        lines.add(new_line)

def append_tr(screen, trees):
    if len(trees) < 11:
        new_tree = Tree(screen)
        trees.add(new_tree)

def move_tr(screen, trees, move):

    for tr in trees.copy():

        if move == "down":
            break

        tr.sec_rect_im.y += 2
        tr.sec_rect_im.x += 10
        tr.sec_im = pygame.transform.scale(tr.sec_im,
                                            (tr.sec_rect_im.width+(tr.sec_rect_im.y//8),
                                             tr.sec_rect_im.height+(tr.sec_rect_im.y//8)))

        tr.rect_im.y += 2
        tr.rect_im.x -= 11
        tr.image = pygame.transform.scale(tr.image,
                                            (tr.sec_rect_im.width+(tr.sec_rect_im.y//10),
                                             tr.sec_rect_im.height+(tr.sec_rect_im.y//10)))

        if tr.rect_im.y >= 620:
            trees.remove(tr)

    if not move == "up":
        for tr in trees.copy():
            tr.sec_rect_im.y += 25
            tr.rect_im.y += 25
