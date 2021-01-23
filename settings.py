from os import getcwd
import pygame
import gf
from os import getcwd
from car import Car
from speedline import Speedline
from road import Background


class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 60

        self.sound = getcwd()+"\\music\\strange.mp3"
        self.start_sound = getcwd()+"\\music\\start.mp3"

        self.chords_lines = [
                        #left side (from bottom to mid)
                        [-240, 720], [0, 530], [120, 520], [240, 510], [360, 500], [480, 480], [620, 470],
                        #right side (from mid to bottom)
                        [660, 470], [800, 480], [920, 500], [1040, 510], [1160, 520], [1280, 530], [1520, 720]
                                ]

        self.chords_lines2 = [
                        #left side (from bottom to mid)
                        [0, 720], [320, 560], [380, 540], [440, 520], [500, 500], [560, 480], [620, 470],
                        #right side (from mid to bottom)
                        [660, 470], [700, 480], [780, 500], [840, 520], [900, 540], [960, 560], [1280, 720]
                                ]

        self.chords_bg = [
                        (0, 360), (1280, 360), (1280, 720), (0, 720)
                        ]

        self.color_bg = (150,0,150)
        self.color_rd = (0,0,0)
        self.color_imitate_speed = (45,45,45,196)

class app(Settings):

    g_set = Settings()

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.g_set.res, pygame.HWSURFACE|pygame.DOUBLEBUF)

        self.clock = pygame.time.Clock()
        self.game = False

    def prepare_first_frame(self):
        pygame.mixer.music.load(self.g_set.start_sound)
        pygame.mixer.music.play()

        self.start_im = pygame.image.load(getcwd()+"\\images\\mid.png").convert()
        self.im_rect = self.start_im.get_rect()

        path = pygame.font.match_font('times new roman', True, True)
        font = pygame.font.Font(path, 72)

        return font

    def prepare_main_frame(self):

        self.car = Car(self.screen)
        self.bg = Background(self.screen, self.g_set.color_bg,
                             self.g_set.color_rd, self.g_set.chords_lines,
                             self.g_set.chords_lines2
                             )

    def run(self):

        if not self.game:
            self.first_frame()
        if self.game:
            self.main_frame()

    def first_frame(self):
        tmp = 10
        color = [0, 0, 0]
        font = self.prepare_first_frame()

        text = font.render('W  a  n  g  a  n    M  i  d  n  i  g  h  t', 50, color)
        font_rect = text.get_rect()

        font_rect.centerx, font_rect.centery = 640, 240

        while not self.game:
            self.screen.fill((0,0,0))
            self.screen.blit(self.start_im, self.im_rect)

            gf.check_events()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.im_rect.x -= 50
                font_rect.x += 50

            text = font.render('W  a  n  g  a  n    M  i  d  n  i  g  h  t', 50, color)

            if color[0] > 200: tmp = -10
            if color[0] < 50: tmp = 10

            for i in range(len(color)): color[i] += tmp

            self.screen.blit(text, font_rect)
            pygame.display.update()

            self.clock.tick(self.g_set.FPS)

            if font_rect.x > 1280:
                pygame.mixer.music.load(self.g_set.sound)
                pygame.mixer.music.play()
                self.game = True

    def main_frame(self):

        self.prepare_main_frame()
        chord_x = self.g_set.chords_lines[6][0]
        chord_y = self.g_set.chords_lines[6][1]
        lines = []

        while True:

            self.clock.tick(self.g_set.FPS)

            gf.check_events()

            keys = pygame.key.get_pressed()
            move = gf.check_going(keys)
            gf.check_car_turning(keys, self.car)

            self.bg.draw_background()

            gf.append_l(self.screen, lines, self.g_set.color_imitate_speed,
                        self.g_set.res, chord_y, move)

            [line.draw_lines() for line in lines.copy()]

            gf.imitate_speed(lines, move)

            self.car.blitme()

            pygame.display.update()
