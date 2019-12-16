from speedline import Speedline
import pygame

def check_events(turn,TURNING, MOVE_D, screen, color_imitate_speed, lines, res, bg_y):

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == MOVE_D:
            new_line = Speedline(screen, color_imitate_speed, res, bg_y)
            lines.add(new_line)

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

    return move


def imitate_speed(screen, lines, color, res):

    for line in lines.copy():
        line.rect.y += 4
        line.rect.height += 1

        if line.rect.y >= 720:
            lines.remove(line)
