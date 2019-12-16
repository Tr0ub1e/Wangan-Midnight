import pygame

class Car():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('C:\\Users\\Tr0ub1e\\Desktop\\Wangan Midnight\\images\\car2.png').convert_alpha()
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.centerx - self.rect.centerx
        self.rect.y = self.screen_rect.bottom*0.85




    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update_car(self, move):

        if move == 'right':
            self.rect.x += 10

        if move == 'left':
            self.rect.x -= 10
