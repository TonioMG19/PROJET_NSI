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
    inLevelChoice = False
    has_enter = False
    inMap1 = False
    inMap2 = False
    inMap3 = False
    floor = 1


    player = Player()

    window.blit(background,(0,0))

    mapIntro1 = loadMap("mapIntro-1.txt")
    default_mapIntro1 = loadMap("mapIntro-1.txt")
    mapIntro2 = loadMap("mapIntro-2.txt")
    default_mapIntro2 = loadMap("mapIntro-2.txt")
    map1 = loadMap("map1.txt")
    default_map1 = loadMap("map1.txt")
    map2 = loadMap("map2.txt")
    default_map2 = loadMap("map2.txt")
    map3 = loadMap("map3.txt")
    default_map3 = loadMap("map3.txt")

    i = 0

    while True:

        if inMenu:
            pygame.display.set_caption("Escape the tower - Menu")
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
                        inLevelChoice = True

        if inLevelChoice:
            pygame.display.set_caption("Escape the tower - Choix du niveau")
            window.blit(level_choice, (0, 0))
            window.blit(intro, (256, 266))
            window.blit(one, (226, 516))
            window.blit(two, (576, 516))
            window.blit(three, (926, 516))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 256 and pos[0] <= 1024 and pos[1] >= 266 and pos[1] <= 394:
                        inLevelChoice = False
                        floor = 1
                        inIntro = True
                    elif pos[0] >= 226 and pos[0] <= 354 and pos[1] >= 516 and pos[1] <= 644:
                        inLevelChoice = False
                        floor = 1
                        inMap1 = True
                    elif pos[0] >= 576 and pos[0] <= 704 and pos[1] >= 516 and pos[1] <= 644:
                        inLevelChoice = False
                        floor = 1
                        inMap2 = True
                    elif pos[0] >= 926 and pos[0] <= 1054 and pos[1] >= 516 and pos[1] <= 644:
                        inLevelChoice = False
                        floor = 1
                        inMap3 = True


        if inIntro or inMap1 or inMap2 or inMap3:

            if inIntro:
                pygame.display.set_caption("Escape the tower - Introduction")
                if floor == 1:
                    map = mapIntro1
                elif floor == 2:
                    map = mapIntro2
            if inMap1:
                pygame.display.set_caption("Escape the tower - Niveau 1")
                map = map1
            if inMap2:
                pygame.display.set_caption("Escape the tower - Niveau 2")
                map = map2
            if inMap3:
                pygame.display.set_caption("Escape the tower - Niveau 3")
                map = map3

            window.blit(background, (0, 0))
            drawMap(map, window, brick_x, ladder, door, trappe, key, closed_trap)
            window.blit(player.IMG, player.rect)

            if has_enter:
                window.blit(won, (256, 234))

            pygame.display.update()

            if player.rect.y < 896:
                if(map[round((player.rect.y + 64) / 64)][round(player.rect.x/ 64)]) == 'o' and (i == 0 or i % 5 == 0) and (map[round((player.rect.y)/ 64)][round(player.rect.x/ 64)]) != '#' and (map[round((player.rect.y)/ 64)][round(player.rect.x/ 64)]) != 't':
                    i += 1
                    player.move_down(map)
                elif (map[round((player.rect.y + 64) / 64)][round(player.rect.x / 64)]) == 'o':
                    i += 1
            else:
                i = 0

            if map[round(player.rect.y / 64)][round(player.rect.x / 64)] == 'k':
                player.has_key = True
                open_trappe(map)
                map[round(player.rect.y / 64)] = map[round(player.rect.y / 64)][:round(player.rect.x / 64)] + 'o' + map[round(player.rect.y / 64)][round(player.rect.x / 64)+1:]

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
                    elif event.key == pygame.K_INSERT:
                        player.rect.y = 128
                        player.rect.x = 256
                    elif event.key == pygame.K_RETURN:
                        if map[round(player.rect.y / 64)][round(player.rect.x / 64)] == 'p':
                            if inIntro:
                                if has_enter:
                                    inIntro = False
                                    inLevelChoice = True
                                    player.reset()
                                    mapIntro1 = reset_map(map, default_mapIntro1)
                                    mapIntro2 = reset_map(map, default_mapIntro2)
                                    has_enter = False
                                else:
                                    has_enter = True
                            if inMap1:
                                if has_enter:
                                    inMap1 = False
                                    inLevelChoice = True
                                    player.reset()
                                    reset_map(map, default_map1)
                                    has_enter = False
                                else:
                                    has_enter = True
                            if inMap2:
                                if has_enter:
                                    inMap2 = False
                                    inLevelChoice = True
                                    player.reset()
                                    reset_map(map, default_map2)
                                    has_enter = False
                                else:
                                    has_enter = True
                            if inMap3:
                                if has_enter:
                                    inMap3 = False
                                    inLevelChoice = True
                                    player.reset()
                                    reset_map(map, default_map3)
                                    has_enter = False
                                else:
                                    has_enter = True
                        if map[round(player.rect.y / 64)][round(player.rect.x / 64)] == 't':
                            if round(player.rect.y / 64) == 0:
                                if inIntro:
                                    floor = 2
                                    player.rect.y = 832
                                if inMap1:
                                    pass
                                if inMap2:
                                    pass
                                if inMap3:
                                    pass
                                pass
                            if round(player.rect.y / 64) == 14:
                                if inIntro:
                                    floor = 1
                                    player.rect.y = 0
                                if inMap1:
                                    pass
                                if inMap2:
                                    pass
                                if inMap3:
                                    pass
                                pass


if __name__ == "__main__":
    main()