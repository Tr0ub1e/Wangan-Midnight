import pygame
from os import getcwd

class Car():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load(getcwd()+"\\images\\nissan.png").convert()
        self.image.set_colorkey((255,255,255))

        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.centerx - self.rect.centerx
        self.rect.y = self.screen_rect.bottom - (self.rect.height)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
