import pygame

pygame.init()

background = pygame.image.load("assets/brick-wall.jpg")
brick_x = pygame.image.load("assets/brick_x.jpg")
brick_o = pygame.image.load("assets/brick_o.png")
ladder = pygame.image.load("assets/construction.png")
menu = pygame.image.load("assets/menu.png")
logo = pygame.image.load("assets/logo.png")
start = pygame.image.load("assets/arrows.png")
door = pygame.image.load("assets/door.png")
tower = pygame.image.load("assets/tower.png")
levels = pygame.transform.scale(pygame.image.load("assets/button_level.png"), (388, 146))
credit = pygame.transform.scale(pygame.image.load("assets/button_credit.png"), (388, 146))
won = pygame.image.load("assets/won.png")