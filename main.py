import pygame
import random
import math
import os
import time
from functions import *
from player import Player

pygame.init()
pygame.font.init()

def menu():
    inMenu = True
    while inMenu:
        window.blit()

def main():

    window = pygame.display.set_mode((1280, 960))

    player = Player()

    background = pygame.image.load("assets/brick-wall.jpg")
    brick_x = pygame.image.load("assets/brick_x.jpg")
    brick_o = pygame.image.load("assets/brick_o.png")
    ladder = pygame.image.load("assets/construction.png")

    window.blit(background,(0,0))

    map = loadMap("map.txt")

    drawMap(map, window, brick_o, brick_x,ladder)

    while True:

        window.blit(background, (0, 0))
        drawMap(map, window, brick_o, brick_x,ladder)
        window.blit(player.IMG, player.rect)

        pygame.display.update()

        if(map[round((player.rect.y + 64 )/ 64)][round(player.rect.x/ 64)]) == 'o':
            player.move_down(map)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right(map)
                elif event.key == pygame.K_LEFT:
                    player.move_left(map)
                elif event.key == pygame.K_DOWN:
                    player.move_down(map)
                elif event.key == pygame.K_UP:
                    player.move_up(map)

if __name__ == "__main__":
    main()