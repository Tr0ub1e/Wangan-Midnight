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

    def draw_background(self):
        self.bg_rect = pygame.Rect(0, self.chords_rd[6][1], 1280, 350)

        self.screen.blit(self.im_bg, self.rect_im)
        pygame.draw.rect(self.screen, self.color_bg, self.bg_rect)

        pygame.draw.polygon(self.screen, (0,0,0), (self.chords_rd[0], self.chords_rd[1], self.chords_rd[-2], self.chords_rd[-1]))
        pygame.draw.polygon(self.screen, (0,0,0), (self.chords_rd[1], self.chords_rd[2], self.chords_rd[-3], self.chords_rd[-2]))
        pygame.draw.polygon(self.screen, (0,0,0), (self.chords_rd[2], self.chords_rd[3], self.chords_rd[-4], self.chords_rd[-3]))
        pygame.draw.polygon(self.screen, (0,0,0), (self.chords_rd[3], self.chords_rd[4], self.chords_rd[-5], self.chords_rd[-4]))
        pygame.draw.polygon(self.screen, (0,0,0), (self.chords_rd[4], self.chords_rd[5], self.chords_rd[-6], self.chords_rd[-5]))
        pygame.draw.polygon(self.screen, (0,0,0), (self.chords_rd[5], self.chords_rd[6], self.chords_rd[-7], self.chords_rd[-6]))


    def make_hills(self, run):
        dx = -8
        ddy = 1

        if run and self.chords_rd[6][0] > 520:
            k = 1
            for i in range(1, (len(self.chords_rd)//2)):

                self.chords_rd[k][0] += dx
                self.chords_rd[-k-1][0] -= dx

                if k < 2:

                    self.chords_rd[7-k][1] += ddy
                    self.chords_rd[6+k][1] += ddy

                elif k > 3:

                    self.chords_rd[7-k][1] += ddy
                    self.chords_rd[6+k][1] += ddy

                k += 1
            #print(self.chords_rd)

        if run == False and self.chords_rd[6][0] < 600:
            k = 1
            for i in range(1, (len(self.chords_rd)//2)):

                self.chords_rd[k][0] -= dx
                self.chords_rd[-k-1][0] += dx

                if k < 2:

                    self.chords_rd[7-k][1] -= ddy
                    self.chords_rd[6+k][1] -= ddy

                elif k > 3:

                    self.chords_rd[7-k][1] -= ddy
                    self.chords_rd[6+k][1] -= ddy

                k += 1
#            print(self.chords_rd)

        return self.chords_rd[6][0], self.chords_rd[6][1]



    def make_turns(self, turn):
        pass
"""
if run and self.chords_rd[6][0] > 520:

    for i in range(1, (len(self.chords_rd)//2)):

        self.chords_rd[k][0] += dx
        self.chords_rd[-k-1][0] -= dx

        if k < 2:

            self.chords_rd[7-k][1] += ddy
            self.chords_rd[6+k][1] += ddy

        elif k > 3:

            self.chords_rd[7-k][1] += ddy
            self.chords_rd[6+k][1] += ddy

        k += 1
"""
