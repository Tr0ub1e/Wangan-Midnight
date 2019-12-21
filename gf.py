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


    if move == "up":
        for line in lines.copy():
            line.rect.y += 100





def append_l(screen, lines, color, res, move):
    if len(lines) < 5:
        new_line = Speedline(screen, color, res)
        lines.add(new_line)
