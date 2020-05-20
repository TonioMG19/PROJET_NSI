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
pygame.display.set_caption("Escape the tower")
pygame.display.set_icon(tower)

def main():

    inMenu = True
    inIntro = False


    player = Player()

    window.blit(background,(0,0))

    map = loadMap("map.txt")

    drawMap(map, window, brick_o, brick_x, ladder, door)

    i = 0

    inMap1 = False
    inMap2 = False
    inMap3 = False

    while True:

        if inMenu:
            window.blit(menu, (0, 0))
            window.blit(logo, (256, -40))
            window.blit(levels, (446, 480))
            window.blit(credit, (446,700))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 446 and pos[0] <= 834 and pos[1] >= 480 and pos[1] <= 626:
                        inMenu = False
                        inIntro = True

        if inIntro or inMap1 or inMap2 or inMap3:

            window.blit(background, (0, 0))
            drawMap(map, window, brick_o, brick_x, ladder, door)
            window.blit(player.IMG, player.rect)

            pygame.display.update()

            if(map[round((player.rect.y + 64) / 64)][round(player.rect.x/ 64)]) == 'o' and (i == 0 or i % 5 == 0) and (map[round((player.rect.y)/ 64)][round(player.rect.x/ 64)]) != '#':
                i += 1
                player.move_down(map)
            elif (map[round((player.rect.y + 64) / 64)][round(player.rect.x / 64)]) == 'o':
                i += 1
            else:
                i = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.move_right(map)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        player.move_left(map)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.move_down(map)
                    elif event.key == pygame.K_UP or event.key == pygame.K_z:
                        player.move_up(map)
                    elif event.key == pygame.K_RETURN and map[round(player.rect.y / 64)][round(player.rect.x/ 64)] == 'p':
                        if inIntro:
                            inIntro = False
                            inMenu = True
                            player.reset_place()



if __name__ == "__main__":
    main()