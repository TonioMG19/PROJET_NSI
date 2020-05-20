import pygame
import random
import math
import os
import time
from functions import *
from player import Player

pygame.init()
pygame.font.init()

def main():

    window = pygame.display.set_mode((1280, 960))

    player = Player()

    background = pygame.image.load("assets/brick-wall.jpg")
    brick_x = pygame.image.load("assets/brick_x.jpg")
    brick_o = pygame.image.load("assets/brick_o.png")

    window.blit(background,(0,0))

    drawMap("map.txt", window, brick_o, brick_x)

    while True:

        window.blit(background, (0, 0))
        drawMap("map.txt", window, brick_o, brick_x)
        window.blit(player.IMG, player.rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                print("KEydown")
                if event.key == pygame.K_RIGHT:
                    print("K RIGHT")
                    player.move_right()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_DOWN:
                    player.move_down()
                elif event.key == pygame.K_UP:
                    player.move_up()

if __name__ == "__main__":
    main()