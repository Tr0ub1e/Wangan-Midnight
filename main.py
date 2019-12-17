import pygame
import gf
from settings import Settings
from car import Car
from speedline import Speedline
from road import Background


def main():
    pygame.init()
    g_set = Settings()
    bg_y = g_set.chords_lines[3][1]

    turn = 'center'

    screen = pygame.display.set_mode(g_set.res, pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
    pygame.mixer.music.load(g_set.sound)
    pygame.mixer.music.play(start=131)

    clock = pygame.time.Clock()

    car = Car(screen)
    bg = Background(screen, g_set.color_bg, g_set.color_rd, g_set.res, g_set.chords_lines)
    lines = pygame.sprite.Group()

    MOVE_D = pygame.USEREVENT + 1
    TURNING = pygame.USEREVENT + 2

    pygame.time.set_timer(TURNING, 2000)
    pygame.time.set_timer(MOVE_D, 500)

    while True:

        clock.tick(g_set.FPS)

        turn = gf.check_events(turn, TURNING, MOVE_D, screen, g_set.color_imitate_speed, lines, g_set.res, bg_y)

        keys = pygame.key.get_pressed()
        move = gf.check_keydown_events(keys)

        bg.draw_background()
        bg_y = bg.make_hills()
        bg.make_turns(turn)

        gf.imitate_speed(screen, lines, g_set.color_rd, g_set.res)

        for line in lines.copy():
            line.draw_lines()

        car.blitme()
        car.update_car(move)

        pygame.display.flip()

if __name__ == '__main__':
    main()
