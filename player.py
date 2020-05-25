import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    IMG = pygame.image.load("assets/people.png")

    def __init__(self):
        super().__init__()
        self.rect = self.IMG.get_rect()
        self.rect.x = 64
        self.rect.y = 832
        self.pressed = {}
        self.begin_rect_x = 64
        self.begin_rect_y = 832
        self.has_key = False

    def move_right(self,map):
        if map[round(self.rect.y/64)][round((self.rect.x+64)/64)] != 'x':
            self.rect.x += 64

    def move_left(self,map):
        if map[round(self.rect.y / 64)][round((self.rect.x - 64) / 64)] != 'x':
            self.rect.x -= 64

    def move_up(self,map):
        if map[round((self.rect.y - 64 )/ 64)][round(self.rect.x/ 64)] != 'x' and self.rect.y > 0 and (map[round(self.rect.y/64)][round(self.rect.x/64)] == '#' or map[round(self.rect.y/64)][round(self.rect.x/64)] == 't'):
            self.rect.y -= 64

    def move_down(self,map):
        if self.rect.y < 896:
            if map[round((self.rect.y + 64 )/ 64)][round(self.rect.x/ 64)] != 'x':
                self.rect.y += 64

    def reset(self):
        self.rect.x , self.rect.y = self.begin_rect_x, self.begin_rect_y
        self.has_key = False