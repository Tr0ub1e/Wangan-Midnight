import pygame
from os import getcwd
from pygame.sprite import Sprite

class Car(Sprite):

    def __init__(self, screen):
        super(Car, self).__init__()
        self.screen = screen

        self.image = pygame.image.load(getcwd()+"\\images\\tengu\\tengu_1.png").convert()
        self.imagedef = pygame.image.load(getcwd()+"\\images\\tengu\\tengu_1.png").convert()
        self.imagedef.set_colorkey((0,0,0))


        self.image_l = pygame.image.load(getcwd()+"\\images\\tengu\\tengu_5.png").convert()
        self.image_r = pygame.image.load(getcwd()+"\\images\\tengu\\tengu_2.png").convert()
        self.image_l.set_colorkey((0,0,0))
        self.image_r.set_colorkey((0,0,0))

        self.image_l_dr = pygame.image.load(getcwd()+"\\images\\tengu\\tengu_7.png").convert()
        self.image_r_dr = pygame.image.load(getcwd()+"\\images\\tengu\\tengu_4.png").convert()
        self.image_l_dr.set_colorkey((0,0,0))
        self.image_r_dr.set_colorkey((0,0,0))

        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.centerx - self.rect.centerx
        self.rect.y = self.screen_rect.bottom - (self.rect.height)

        self.scal = [25, 15]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def car_move(self, move):
        keys = pygame.key.get_pressed()
        if move == 'right' and self.rect.x < 1180:
            if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
                self.image = self.image_r_dr
                i = 15
            else:
                self.image = self.image_r
                i = 20
            self.rect.x += i

        if move == 'left' and self.rect.x > 0:
            if keys[pygame.K_SPACE] and keys[pygame.K_LEFT]:
                self.image = self.image_l_dr
                i = 15
            else:
                self.image = self.image_l
                i = 20
            self.rect.x -= i

        if not move == 'left' and not move == 'right':
            self.image = self.imagedef

    def stay_road(self, turn):

        if turn == 'right' and self.rect.x > 0:
            self.rect.x -= 10

        if turn == 'left' and self.rect.x < 1280:
            self.rect.x += 10
