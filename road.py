import pygame


class Background():

    def __init__(self, screen, color_bg, color_rd, res, route, chords_rd=[]):

        self.screen = screen
        self.im_bg = pygame.image.load("C:\\Users\\Tr0ub1e\\Desktop\\Wangan Midnight\\images\\city.jpg").convert()
        self.rect_im = self.im_bg.get_rect()
        self.rect_im.top = -100

        self.color_bg = color_bg
        self.color_rd = color_rd
        self.color_ln = (127,255,0)
        self.res = res
        self.chords_rd = chords_rd
        self.route = route

        self.bg_rect = pygame.Rect(0, self.chords_rd[3][1], 1280, 200)

    def draw_background(self):

        self.screen.blit(self.im_bg, self.rect_im)
        pygame.draw.rect(self.screen, self.color_bg, self.bg_rect)
        pygame.draw.polygon(self.screen, self.color_rd, (self.chords_rd[0], self.chords_rd[1], self.chords_rd[2],
                            self.chords_rd[3], self.chords_rd[4], self.chords_rd[5]))


        pygame.draw.lines(self.screen, self.color_ln, False, [self.chords_rd[0], self.chords_rd[1], self.chords_rd[2]], 3)
        pygame.draw.lines(self.screen, self.color_ln, False, [self.chords_rd[3], self.chords_rd[4], self.chords_rd[5]], 3)


    def make_hills(self):

        if self.route == True:

            self.chords_rd[2][1] -= 1
            self.chords_rd[3][1] -= 1

            self.chords_rd[2][0] += 1
            self.chords_rd[3][0] -= 1

            self.rect_im.y -= 1
            self.bg_rect.y -= 1

            if self.chords_rd[2][1] <= 360:

                self.route = False

        if self.route == False:

            self.chords_rd[2][1] += 1
            self.chords_rd[3][1] += 1

            self.chords_rd[2][0] -= 1
            self.chords_rd[3][0] += 1

            self.rect_im.y += 1
            self.bg_rect.y += 1

            if self.chords_rd[2][1] >= 515:
                self.route = True

        return self.chords_rd[2][1]
