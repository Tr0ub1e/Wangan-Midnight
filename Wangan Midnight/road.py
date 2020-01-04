import pygame
from os import getcwd

class Background():

    def __init__(self, screen, color_bg, color_rd, chords_rd=[]):

        self.screen = screen
        self.im_bg = pygame.image.load(getcwd()+"\\images\\city.bmp").convert_alpha()
        self.rect_im = self.im_bg.get_rect()
        self.rect_im.top = -100
        self.rect_im.centerx = 640

        self.color_bg = color_bg
        self.color_rd = color_rd
        self.color_ln = (192, 192, 192)
        #self.res = res
        self.chords_rd = chords_rd
        self.route = True

        self.bg_rect = pygame.Rect(0, self.chords_rd[6][1], 1280, 350)

    def draw_background(self):

        self.screen.blit(self.im_bg, self.rect_im)
        pygame.draw.rect(self.screen, self.color_bg, self.bg_rect)
        pygame.draw.polygon(self.screen, self.color_rd, (self.chords_rd[0], self.chords_rd[1], self.chords_rd[2], self.chords_rd[3], self.chords_rd[4],
                                                            self.chords_rd[5], self.chords_rd[6], self.chords_rd[7], self.chords_rd[8], self.chords_rd[9],
                                                            self.chords_rd[10], self.chords_rd[11], self.chords_rd[12], self.chords_rd[13]))




    def make_hills(self):
        pass

        return self.chords_rd[3][1]


    def make_turns(self, turn):
        dx = 4

        if turn == 'left':

            for i in self.chords_rd:

                if self.chords_rd[1][0] > 0:
                    i[0] -= dx
                    dx += 3

                if self.chords_rd.index(i) >= (len(self.chords_rd)/2)-1:
                    dx -= 7

        if turn == 'center':

            for i in self.chords_rd:

                if self.chords_rd[1][0] > 100:
                    i[0] += dx
                    dx += 3

                if self.chords_rd.index(i) >= (len(self.chords_rd)/2)-1:
                    dx -= 7

        if turn == 'right':
            dx = 4
            for i in self.chords_rd:

                if self.chords_rd[12][0] < 1280:
                    i[0] += dx
                    dx += 7

                if self.chords_rd.index(i) >= (len(self.chords_rd)/2)-1:
                    dx -= 3
