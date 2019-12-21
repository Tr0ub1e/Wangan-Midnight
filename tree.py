import pygame
from pygame.sprite import Sprite


class Tree(Sprite):

    def __init__(self, screen, color, res):
        super(Tree, self).__init__()

        self.screen = screen
        self.image = image
        self.rect_im = self.image.get_rect()


    def draw_trees(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
