import pygame
from pygame.sprite import Sprite


class Speedline(Sprite):

    def __init__(self, screen, color, res):
        super(Speedline, self).__init__()

        self.screen = screen
        self.color = color
        #self.y_line = y_line

        self.rect = pygame.Rect(0, res[1]/2, res[0], 1)
        #print(self.rect)

    def draw_lines(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
