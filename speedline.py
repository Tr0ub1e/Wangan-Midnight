import pygame
from pygame.sprite import Sprite


class Speedline(Sprite):

    def __init__(self, screen, color, res, bg_y):
        super(Speedline, self).__init__()

        self.screen = screen
        self.color = color
        self.bg_y = bg_y

        self.rect = pygame.Rect(0, self.bg_y, res[0], 0)

    def draw_lines(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
