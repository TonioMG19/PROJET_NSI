import pygame
import random
import math
import os
import time
from functions import *
from player import Player
from images import *

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((1280, 960))

def main():

    inMenu = True

    while inMenu:
        window.blit(menu,(0,0))
        window.blit(logo,(256,-40))
        window.blit(start,(543,700))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 543 and pos[0] <= 738 and pos[1] >= 700 and pos[1] <= 895:
                    inMenu = False

    player = Player()

    window.blit(background,(0,0))

    map = loadMap("map.txt")

    drawMap(map, window, brick_o, brick_x,ladder)

    i = 0

    while True:

        window.blit(background, (0, 0))
        drawMap(map, window, brick_o, brick_x,ladder)
        window.blit(player.IMG, player.rect)

        pygame.display.update()

        if(map[round((player.rect.y + 64 )/ 64)][round(player.rect.x/ 64)]) == 'o' and (i == 0 or i%10 == 0):
            i+=1
            player.move_down(map)
        elif (map[round((player.rect.y + 64 )/ 64)][round(player.rect.x/ 64)]) == 'o':
            i+=1
        else:
            i = 0

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