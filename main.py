import pygame
import gf
from settings import Settings
from car import Car
from speedline import Speedline


def main():
    pygame.init()
    g_set = Settings()

    screen = pygame.display.set_mode(g_set.res)
    bg = pygame.image.load("C:\\Users\\Tr0ub1e\\Desktop\\Wangan Midnight\\city2.jpg")
    screen.fill(g_set.color_bg)
    screen.blit(bg, (0,0))

    clock = pygame.time.Clock()
    car = Car(screen)
    lines = pygame.sprite.Group()

    MOVE_D = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVE_D, 500)

    while True:
        clock.tick(g_set.FPS)

        gf.check_events(MOVE_D, screen, g_set.color_imitate_speed, lines, g_set.res)
        
        keys = pygame.key.get_pressed()
        move = gf.check_keydown_events(keys)

        gf.imitate_speed(screen, lines, g_set.color_road, g_set.res)
        gf.draw_lines_road(screen, g_set.color_line, g_set.color_road, g_set.color_bg, g_set.chords_lines)

        for line in lines.copy():
            line.draw_lines()

        #if pygame.time.get_ticks() % 10 == 0:
        #    gf.append_lines(screen, g_set.color_imitate_speed, lines, g_set.res)
        #gf.update_l(lines)

        car.blitme()
        car.update_car(move)

        pygame.display.update()

if __name__ == '__main__':
    main()
