import pygame
from pygame.sprite import Sprite
from os import getcwd



class Tree(Sprite):

    def __init__(self, screen):
        super(Tree, self).__init__()

        self.screen = screen
        self.image = pygame.image.load(getcwd()+"\\images\\tree.png")
        self.sec_im = pygame.image.load(getcwd()+"\\images\\tree.png")

        self.rect_im = self.image.get_rect()
        self.sec_rect_im = self.sec_im.get_rect()

        self.rect_im.centery, self.sec_rect_im.centery = 420, 420
        self.rect_im.centerx, self.sec_rect_im.centerx = 450, 820

    def draw_trees(self):
        self.screen.blit(self.image, self.rect_im)
        self.screen.blit(self.sec_im, self.sec_rect_im)
