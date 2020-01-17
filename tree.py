import pygame
from pygame.sprite import Sprite
from os import getcwd



class Tree(Sprite):

    def __init__(self, screen, bottom, x):
        super(Tree, self).__init__()


        self.screen = screen
        self.image = pygame.image.load(getcwd()+"\\images\\plant-green.png").convert_alpha()
        self.sec_im = pygame.image.load(getcwd()+"\\images\\plant-green.png").convert_alpha()

        self.light = pygame.image.load(getcwd()+"\\images\\light.png").convert_alpha()
        self.light2 = pygame.image.load(getcwd()+"\\images\\light2.png").convert_alpha()


        self.rect_im = self.image.get_rect()
        self.sec_rect_im = self.sec_im.get_rect()

        self.rect_l = self.light.get_rect()
        self.rect_l2 = self.light2.get_rect()


        self.rect_im.bottom = self.sec_rect_im.bottom = bottom
        self.rect_l.bottom = self.rect_l2.bottom = bottom

        self.rect_l.x, self.rect_l2.x = x-self.rect_im.w-self.rect_l.w, (1280 - self.rect_l.x)

        self.rect_im.x = x-self.rect_im.w
        self.sec_rect_im.x = (1280 - self.rect_im.x)

    def draw_trees(self):
        self.screen.blit(self.image, self.rect_im)
        self.screen.blit(self.sec_im, self.sec_rect_im)

        self.screen.blit(self.light, self.rect_l)
        self.screen.blit(self.light2, self.rect_l2)
