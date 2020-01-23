import pygame
import gf
from settings import Settings
from car import Car
from speedline import Speedline
from road import Background
from tree import Tree

def main():
    pygame.init()
    g_set = Settings()

    screen = pygame.display.set_mode(g_set.res, pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
    pygame.mixer.music.load(g_set.sound)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()

    car = Car(screen)
    bg = Background(screen, g_set.color_bg, g_set.color_rd, g_set.chords_lines)

    lines = pygame.sprite.Group()
    trees = pygame.sprite.Group()

    run = None
    i = 0

    chord_x = g_set.chords_lines[6][0]
    chord_y = g_set.chords_lines[6][1]

    while True:
        
        clock.tick(g_set.FPS)

        gf.check_events()

        keys = pygame.key.get_pressed()
        move = gf.check_keydown_events(keys)

        bg.draw_background()

        run = gf.make_map(i)

        chord_x, chord_y = bg.make_hills(run)
        bg.turn_world_around_car(move)

        if i == 4:
            i = 0

        if pygame.time.get_ticks() % 25 == 0:
            i += 1


        gf.append_l(screen, lines, g_set.color_imitate_speed, g_set.res, chord_y, move)

        for line in lines.copy():
            line.draw_lines()

        #for tr in trees.copy():
        #    tr.draw_trees()

        gf.imitate_speed(screen, lines, g_set.color_imitate_speed, g_set.res, move, chord_y)

        #gf.append_tr(screen, trees, chord_y, chord_x)
        #gf.move_tr(screen, trees, move)

        car.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    main()
