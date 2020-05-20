import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    IMG = pygame.image.load("assets/people.png")

    def __init__(self):
        super().__init__()
        self.rect = self.IMG.get_rect()
        self.rect.x = 64
        self.rect.y = 832

    def move_right(self):
        self.rect.x += 64

    def move_left(self):
        self.rect.x -= 64

    def move_up(self):
        self.rect.y -= 64

    def move_down(self):
        self.rect.y += 64