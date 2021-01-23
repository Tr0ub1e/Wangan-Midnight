import pygame
from pygame.sprite import Sprite
from os import getcwd


class Tunnel(Sprite):

    def __init__(self, screen):
        super(Tunnel, self).__init__()

        self.screen = screen

        self.tunnel_l = pygame.image.load(getcwd()+"\\images\\tunnel_a.png").convert_alpha()
        self.tunnel_r = pygame.image.load(getcwd()+"\\images\\tunnel_b.png").convert_alpha()

        self.rect_t_l = self.tunnel_l.get_rect()
        self.rect_t_r = self.tunnel_r.get_rect()

        self.scal = [41, 24]

    def draw_tunnel(self):
        self.screen.blit(self.tunnel_l, self.rect_t_l)
        self.screen.blit(self.tunnel_r, self.rect_t_r)
