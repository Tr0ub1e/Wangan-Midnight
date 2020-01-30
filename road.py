import pygame.gfxdraw as pgf
import pygame
from os import getcwd

class Background():

    def __init__(self, screen, color_bg, color_rd, chords_rd=[], chords_rd2=[]):

        self.screen = screen
        self.im_bg = pygame.image.load(getcwd()+"\\images\\city2.png").convert_alpha()


        self.rect_im = self.im_bg.get_rect()
        self.rect_im.bottom = 600
        self.rect_im.centerx = 640

        self.color_bg = color_bg
        self.color_rd = color_rd
        self.color_ln = (64,255,64)

        self.chords_rd = chords_rd
        self.chords_rd2 = chords_rd2
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


        pgf.bezier(self.screen, (self.chords_rd[0], self.chords_rd[1],
                                    self.chords_rd[2], self.chords_rd[3],
                                        self.chords_rd[4], self.chords_rd[5], self.chords_rd[6]), 7, (255,255,255))

        pgf.bezier(self.screen, (self.chords_rd[-1], self.chords_rd[-2],
                                    self.chords_rd[-3], self.chords_rd[-4],
                                        self.chords_rd[-5], self.chords_rd[-6], self.chords_rd[-7]), 7, (255,255,255))

        pgf.bezier(self.screen, (self.chords_rd2[0], self.chords_rd2[1],
                                    self.chords_rd2[2], self.chords_rd2[3],
                                        self.chords_rd2[4], self.chords_rd2[5], self.chords_rd2[6]), 7, (255,255,255))

        pgf.bezier(self.screen, (self.chords_rd2[-1], self.chords_rd2[-2],
                                    self.chords_rd2[-3], self.chords_rd2[-4],
                                        self.chords_rd2[-5], self.chords_rd2[-6], self.chords_rd2[-7]), 7, (255,255,255))


    def make_hills(self, run):
        dx = -4
        ddy = 0.5

        if run and self.chords_rd[6][1] < 467:
            k = 1
            for i in range(1, (len(self.chords_rd)//2)):

                self.chords_rd[k][0] += dx
                self.chords_rd[-k-1][0] -= dx

                self.chords_rd2[k][0] += dx
                self.chords_rd2[-k-1][0] -= dx

                if k < 2:

                    self.chords_rd[7-k][1] += ddy
                    self.chords_rd[6+k][1] += ddy

                    self.chords_rd2[7-k][1] += ddy
                    self.chords_rd2[6+k][1] += ddy

                elif k > 3:

                    self.chords_rd[7-k][1] += ddy
                    self.chords_rd[6+k][1] += ddy

                    self.chords_rd2[7-k][1] += ddy
                    self.chords_rd2[6+k][1] += ddy

                self.rect_im.y += 1
                k += 1


        if run == False and self.chords_rd[6][1] > 460:
            k = 1
            for i in range(1, (len(self.chords_rd)//2)):

                self.chords_rd[k][0] -= dx
                self.chords_rd[-k-1][0] += dx

                self.chords_rd2[k][0] -= dx
                self.chords_rd2[-k-1][0] += dx

                if k < 2:

                    self.chords_rd[7-k][1] -= ddy
                    self.chords_rd[6+k][1] -= ddy

                    self.chords_rd2[7-k][1] -= ddy
                    self.chords_rd2[6+k][1] -= ddy


                elif k > 3:

                    self.chords_rd[7-k][1] -= ddy
                    self.chords_rd[6+k][1] -= ddy

                    self.chords_rd2[7-k][1] -= ddy
                    self.chords_rd2[6+k][1] -= ddy

                self.rect_im.y -= 1
                k += 1


        return self.chords_rd[6][0], self.chords_rd[6][1]


    def turn_world_around_car(self, move):

        if move == "right":

            dx = -6
            ddx = 6
            k = 0

            for i in range(0, (len(self.chords_rd)//2)):


                self.chords_rd[k][0] += dx
                self.chords_rd[-k-1][0] += dx

                self.chords_rd2[k][0] += dx
                self.chords_rd2[-k-1][0] += dx

                self.chords_rd2[0][0] += dx/4
                self.chords_rd2[-1][0] += dx/4

                dx += ddx
                k += 1

            k = 0
            dx = 30

            for i in range(0, (len(self.chords_rd)//2)):

                self.chords_rd[k][0] -= dx
                self.chords_rd[-k-1][0] -= dx

                self.chords_rd2[k][0] -= dx
                self.chords_rd2[-k-1][0] -= dx

                self.chords_rd2[0][0] -= dx/4
                self.chords_rd2[-1][0] -= dx/4

                self.rect_im.x += 1
                k += 1

        if move == "left":

            dx = -6
            ddx = 6
            k = 0

            for i in range(0, (len(self.chords_rd)//2)):

                self.chords_rd[k][0] -= dx
                self.chords_rd[-k-1][0] -= dx

                self.chords_rd2[k][0] -= dx
                self.chords_rd2[-k-1][0] -= dx

                self.chords_rd2[0][0] -= dx/4
                self.chords_rd2[-1][0] -= dx/4

                dx += ddx
                k += 1

            k = 0
            dx = 30

            for i in range(0, (len(self.chords_rd)//2)):

                self.chords_rd[k][0] += dx
                self.chords_rd[-k-1][0] += dx

                self.chords_rd2[k][0] += dx
                self.chords_rd2[-k-1][0] += dx

                self.chords_rd2[0][0] += dx/4
                self.chords_rd2[-1][0] += dx/4

                self.rect_im.x -= 1
                k += 1
