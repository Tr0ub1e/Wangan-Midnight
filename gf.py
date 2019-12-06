from speedline import Speedline
import pygame

def check_events(MOVE_D, screen, color_imitate_speed, lines, res):

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == MOVE_D:
            append_lines(screen, color_imitate_speed, lines, res)


def check_keydown_events(keys):
    move = None

    if keys[pygame.K_LEFT]:
        move = "left"

    if keys[pygame.K_RIGHT]:
        move = "right"

    return move


def draw_lines_road(screen, color, color_r, color_bg, chords=[]):

    pygame.draw.polygon(screen, color_bg, ((0, 360), (1280, 360), (1280, 720), (0, 720)))

    pygame.draw.polygon(screen, color_r, (chords[0], chords[4], chords[-2], chords[-1]))

    pygame.draw.line(screen, color, chords[0], chords[1], 3)
    pygame.draw.line(screen, color, chords[2], chords[3])
    pygame.draw.line(screen, color, chords[4], chords[5], 3)



def imitate_speed(screen, lines, color, res):

    for line in lines.copy():
        line.rect.y += 4
        line.rect.height += 1

        if line.rect.y > 900:
            lines.remove(line)

def append_lines(screen, color, lines, res):

    new_line = Speedline(screen, color, res)
    lines.add(new_line)

def update_l(lines):
    pass
