import pygame
import gf
import pygame.font as pf
from game_map import g_map
from settings import Settings
from car import Car
from speedline import Speedline
from road import Background

def main():
    pygame.init()
    g_set = Settings()

    screen = pygame.display.set_mode(g_set.res, pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)

    pygame.mixer.music.load(g_set.start_sound)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()

    start_im = pygame.image.load("C:\\Users\\Tr0ub1e\\Desktop\\Folder3\\mid.png").convert()
    im_rect = start_im.get_rect()

    color = [0, 0, 0]

    path = pf.match_font('times new roman', True, True)
    font = pf.Font(path, 72)

    text = font.render('W  a  n  g  a  n    M  i  d  n  i  g  h  t', 50, color)

    font_rect = text.get_rect()
    font_rect.centerx, font_rect.centery = 640, 240

    tmp = 10

    car = Car(screen)
    bg = Background(screen, g_set.color_bg, g_set.color_rd, g_set.chords_lines, g_set.chords_lines2)

    lines = pygame.sprite.Group()
    tunnels = pygame.sprite.Group()
    cars = pygame.sprite.Group()

    run = None
    turn_car = 'normal'
    start = None
    game = False
    i = 0
    raceway = g_map()
    turning = None

    chord_x = g_set.chords_lines[6][0]
    chord_y = g_set.chords_lines[6][1]

    while not game:
        screen.fill((0,0,0))
        screen.blit(start_im, im_rect)
        text = font.render('W  a  n  g  a  n    M  i  d  n  i  g  h  t', 50, color)

        gf.check_events()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            im_rect.x -= 50
            font_rect.x += 50

        if color[0] > 200:
            tmp = -10

        if color[0] < 50:
            tmp = 10

        color[0] += tmp
        color[1] += tmp
        color[2] += tmp

        screen.blit(text, font_rect)
        pygame.display.flip()

        clock.tick(g_set.FPS)

        if font_rect.x > 1280:
            pygame.mixer.music.load(g_set.sound)
            pygame.mixer.music.play()
            game = True


    while game:

        clock.tick(g_set.FPS)

        gf.check_events()

        if pygame.time.get_ticks() < 10000:
            start = False
        else:
            start = True

        if start:
            if pygame.time.get_ticks() % 125 == 0:
                turning = raceway.shutoko_map()


        keys = pygame.key.get_pressed()
        move = gf.check_going(keys)
        turn_car = gf.check_car_turning(keys)

        bg.draw_background()

        x = bg.make_turns(turning)
        gf.append_bots(cars, screen, x)

        gf.append_tun(tunnels, screen, x)

        gf.append_l(screen, lines, g_set.color_imitate_speed, g_set.res, chord_y, move)

        for line in lines.copy():
            line.draw_lines()

        for bot in cars.copy():
            bot.blitme()

        for tun in tunnels.copy():
            tun.draw_tunnel()

        gf.bot_moving(cars)
        gf.tunnel_mov(tunnels)

        gf.imitate_speed(screen, lines, g_set.color_imitate_speed, g_set.res, move, chord_y)

        car.blitme()
        car.stay_road(turning)
        car.car_move(turn_car)

        pygame.display.flip()

if __name__ == '__main__':
    main()
