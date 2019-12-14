from speedline import Speedline
import pygame

def check_events(MOVE_D, screen, color_imitate_speed, lines, res, route, bg_y):

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == MOVE_D:
            append_lines(screen, color_imitate_speed, lines, res, bg_y)

            if route == True:
                route = False
            else:
                route = True


def check_keydown_events(keys):
    move = None

    if keys[pygame.K_LEFT]:
        move = "left"

    if keys[pygame.K_RIGHT]:
        move = "right"

    return move


def imitate_speed(screen, lines, color, res):

    for line in lines.copy():
        line.rect.y += 4
        line.rect.height += 1

        if line.rect.y >= 720:
            lines.remove(line)

def append_lines(screen, color, lines, res, bg_y):

    new_line = Speedline(screen, color, res, bg_y)
    lines.add(new_line)
