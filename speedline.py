import pygame
from pygame.sprite import Sprite

class Speedline(Sprite):

    def __init__(self, screen, color, res, chord):
        super(Speedline, self).__init__()

        self.screen = screen
        self.color = color
        self.chord = chord

        self.ddy = 1


        self.surf = pygame.Surface((1280, 1), pygame.SRCALPHA|pygame.RESIZABLE)
        self.surf.fill(self.color)

        self.rect = self.surf.get_rect()
        self.rect.y = self.chord



    def draw_lines(self):
        self.screen.blit(self.surf, self.rect)
