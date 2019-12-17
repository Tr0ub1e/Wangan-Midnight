import pygame
from os import getcwd

class Background():

    def __init__(self, screen, color_bg, color_rd, res, chords_rd=[]):

        self.screen = screen
        self.im_bg = pygame.image.load(getcwd()+"\\images\\city.jpg").convert()
        self.rect_im = self.im_bg.get_rect()
        self.rect_im.top = -100

        self.color_bg = color_bg
        self.color_rd = color_rd
        self.color_ln = (255, 255, 255)
        self.res = res
        self.chords_rd = chords_rd
        self.route = True

        self.bg_rect = pygame.Rect(0, self.chords_rd[3][1], 1280, 350)

    def draw_background(self):

        self.screen.blit(self.im_bg, self.rect_im)
        pygame.draw.rect(self.screen, self.color_bg, self.bg_rect)
        pygame.draw.polygon(self.screen, self.color_rd, (self.chords_rd[0], self.chords_rd[1], self.chords_rd[2], self.chords_rd[3],
                            self.chords_rd[4], self.chords_rd[5], self.chords_rd[6], self.chords_rd[7]))


        pygame.draw.lines(self.screen, self.color_ln, False, [self.chords_rd[0], self.chords_rd[1], self.chords_rd[2], self.chords_rd[3]], 3)
        pygame.draw.lines(self.screen, self.color_ln, False, [self.chords_rd[4], self.chords_rd[5], self.chords_rd[6], self.chords_rd[7]], 3)


    def make_hills(self):

        if self.route == True:

            self.chords_rd[0][1] -= 1
            self.chords_rd[1][1] -= 1
            self.chords_rd[2][1] -= 1
            self.chords_rd[3][1] -= 1

            self.chords_rd[4][1] -= 1
            self.chords_rd[5][1] -= 1
            self.chords_rd[6][1] -= 1
            self.chords_rd[7][1] -= 1

            self.rect_im.y -= 1
            self.bg_rect.y -= 1

            if self.chords_rd[3][1] <= 515:

                self.route = False

        if self.route == False:

            self.chords_rd[0][1] += 1
            self.chords_rd[1][1] += 1
            self.chords_rd[2][1] += 1
            self.chords_rd[3][1] += 1

            self.chords_rd[4][1] += 1
            self.chords_rd[5][1] += 1
            self.chords_rd[6][1] += 1
            self.chords_rd[7][1] += 1

            self.rect_im.y += 1
            self.bg_rect.y += 1

            if self.chords_rd[3][1] >= 575:

                self.route = True

        return self.chords_rd[3][1]


    def make_turns(self, turn):

        if turn == 'right':

            if self.chords_rd[1][0] < 280:

                self.chords_rd[0][0] += 2
                self.chords_rd[1][0] += 1
                self.chords_rd[2][0] += 3
                self.chords_rd[3][0] += 6

                self.chords_rd[4][0] += 6
                self.chords_rd[5][0] += 3
                self.chords_rd[6][0] += 1
                self.chords_rd[7][0] -= 2

        if turn == 'left':

            if self.chords_rd[1][0] > 110:

                self.chords_rd[1][0] -= 1
                self.chords_rd[2][0] -= 3
                self.chords_rd[3][0] -= 6

                self.chords_rd[4][0] -= 6
                self.chords_rd[5][0] -= 3
                self.chords_rd[6][0] -= 1
                self.chords_rd[7][0] += 1

        if turn == 'center':

            if self.chords_rd[1][0] < 195:

                self.chords_rd[0][0] -= 2
                self.chords_rd[1][0] += 1
                self.chords_rd[2][0] += 3
                self.chords_rd[3][0] += 6

                self.chords_rd[4][0] += 6
                self.chords_rd[5][0] += 3
                self.chords_rd[6][0] += 1
