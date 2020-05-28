'''IMPORTATIONS'''

import pygame
import random
import math
import os
import time
import json
from functions import *
from player import Player
from images import *

'''INITIALISATIONS'''

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('assets/Cunia.otf', 50)

window = pygame.display.set_mode((1280, 960))
pygame.display.set_caption("Escape the tower")
pygame.display.set_icon(tower)

'''FONCTION MAIN, DEROULEMENT DU JEU EN ENTIER'''

def main():

    '''INITIALISATIONS'''

    status = loadAdvance()

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
    map1_1 = loadMap("map1-1.txt")
    default_map1_1 = loadMap("map1-1.txt")
    map1_2 = loadMap("map1-2.txt")
    default_map1_2 = loadMap("map1-2.txt")
    map2_1 = loadMap("map2-1.txt")
    default_map2_1 = loadMap("map2-1.txt")
    map2_2 = loadMap("map2-2.txt")
    default_map2_2 = loadMap("map2-2.txt")
    map3 = loadMap("map3.txt")
    default_map3 = loadMap("map3.txt")

    i = 0

    '''BOUCHE TANT QUE LE JEU EST ACTIF'''

    while True:

        '''MENU'''

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

        '''CHOIX DU NIVEAU'''

        if inLevelChoice:
            if status['intro'] == "Finish":
                mapIntrostatus = myfont.render('Finished !', False, (0, 0, 0))
            elif status['intro'] == "Not":
                mapIntrostatus = myfont.render('Not finished', False, (0, 0, 0))
            if status['map1'] == "Finish":
                map1status = myfont.render('Finished !', False, (0, 0, 0))
            elif status['map1'] == "Not":
                map1status = myfont.render('Not finished', False, (0, 0, 0))
            if status['map2'] == "Finish":
                map2status = myfont.render('Finished !', False, (0, 0, 0))
            elif status['map2'] == "Not":
                map2status = myfont.render('Not finished', False, (0, 0, 0))
            if status['map3'] == "Finish":
                map3status = myfont.render('Finished !', False, (0, 0, 0))
            elif status['map3'] == "Not":
                map3status = myfont.render('Not finished', False, (0, 0, 0))

            pygame.display.set_caption("Escape the tower - Choix du niveau")
            window.blit(level_choice, (0, 0))
            window.blit(intro, (256, 266))
            window.blit(mapIntrostatus, (546, 416))
            window.blit(one, (226, 516))
            window.blit(map1status, (200,666))
            window.blit(two, (576, 516))
            window.blit(map2status, (550, 666))
            window.blit(three, (926, 516))
            window.blit(map3status, (900, 666))

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
        '''EN JEU'''
        '''INITIALISATIONS'''
        if inIntro or inMap1 or inMap2 or inMap3:
            if inIntro:
                pygame.display.set_caption("Escape the tower - Introduction")
                if floor == 1:
                    map = mapIntro1
                elif floor == 2:
                    map = mapIntro2
            if inMap1:
                pygame.display.set_caption("Escape the tower - Niveau 1")
                if floor == 1:
                    map = map1_1
                elif floor == 2:
                    map = map1_2
            if inMap2:
                pygame.display.set_caption("Escape the tower - Niveau 2")
                if floor == 1:
                    map = map2_1
                elif floor == 2:
                    map = map2_2
            if inMap3:
                pygame.display.set_caption("Escape the tower - Niveau 3")
                map = map3

            window.blit(background, (0, 0))
            drawMap(map, window, brick_x, ladder, door, trappe, key, closed_trap)
            window.blit(player.IMG, player.rect)
            window.blit(close, (0,0))
            window.blit(reset,(96,0))

            if has_enter:
                window.blit(won, (256, 234))

            pygame.display.update()

            '''CHUTE'''

            if map[round(player.rect.y / 64)][round(player.rect.x / 64)] == 'k':
                open_trappe(map)
                map[round(player.rect.y / 64)] = map[round(player.rect.y / 64)][:round(player.rect.x / 64)] + 'o' + map[round(player.rect.y / 64)][round(player.rect.x / 64)+1:]

            if player.rect.y < 896:
                if map[round((player.rect.y + 64) / 64)][round(player.rect.x/ 64)] == 'o' and (i == 0 or i % 5 == 0) and (map[round((player.rect.y)/ 64)][round(player.rect.x/ 64)]) != '#' and (map[round((player.rect.y)/ 64)][round(player.rect.x/ 64)]) != 't' or map[round((player.rect.y + 64) / 64)][round(player.rect.x/ 64)] == 'k':
                    i += 1
                    player.move_down(map)
                elif (map[round((player.rect.y + 64) / 64)][round(player.rect.x / 64)]) == 'o':
                    i += 1
            else:
                i = 0

            '''EVENT'''

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 0 and pos[0] <= 64 and pos[1] >= 0 and pos[1] <= 64:
                        mapIntro1 = reset_map(map, default_mapIntro1)
                        mapIntro2 = reset_map(map, default_mapIntro2)
                        map1_1 = reset_map(map, default_map1_1)
                        map1_2 = reset_map(map, default_map1_2)
                        map2_1 = reset_map(map, default_map2_1)
                        map2_2 = reset_map(map, default_map2_2)
                        map3 = reset_map(map, default_map3)
                        player.reset()
                        inIntro = False
                        inMap1 = False
                        inMap2 = False
                        inMap3 = False
                        inLevelChoice = True
                    if pos[0] >= 96 and pos[0] <= 160 and pos[1] >= 0 and pos[1] <= 64:
                        mapIntro1 = reset_map(map, default_mapIntro1)
                        mapIntro2 = reset_map(map, default_mapIntro2)
                        map1_1 = reset_map(map, default_map1_1)
                        map1_2 = reset_map(map, default_map1_2)
                        map2_1 = reset_map(map, default_map2_1)
                        map2_2 = reset_map(map, default_map2_2)
                        map3 = reset_map(map, default_map3)
                        player.reset()
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
                                    status['intro'] = "Finish"
                                    saveAdvance(status)
                                    has_enter = False
                                else:
                                    has_enter = True
                            if inMap1:
                                if has_enter:
                                    inMap1 = False
                                    inLevelChoice = True
                                    player.reset()
                                    map1_1 = reset_map(map, default_map1_1)
                                    map1_2 = reset_map(map, default_map1_2)
                                    status['map1'] = 'Finish'
                                    saveAdvance(status)

                                    has_enter = False
                                else:
                                    has_enter = True
                            if inMap2:
                                if has_enter:
                                    inMap2 = False
                                    inLevelChoice = True
                                    player.reset()
                                    map2_1 = reset_map(map, default_map2_1)
                                    map2_2 = reset_map(map, default_map2_2)
                                    status['map2'] = "Finish"
                                    saveAdvance(status)
                                    has_enter = False
                                else:
                                    has_enter = True
                            if inMap3:
                                if has_enter:
                                    inMap3 = False
                                    inLevelChoice = True
                                    player.reset()
                                    map3 = reset_map(map, default_map3)
                                    status['map3'] = "Finish"
                                    saveAdvance(status)
                                    has_enter = False
                                else:
                                    has_enter = True
                        if map[round(player.rect.y / 64)][round(player.rect.x / 64)] == 't':
                            if round(player.rect.y / 64) == 0:
                                if inIntro:
                                    floor = 2
                                    player.rect.y = 832
                                if inMap1:
                                    floor = 2
                                    player.rect.y = 832
                                if inMap2:
                                    floor = 2
                                    player.rect.y = 832
                                if inMap3:
                                    pass
                                pass
                            if round(player.rect.y / 64) == 14:
                                if inIntro:
                                    floor = 1
                                    player.rect.y = 0
                                if inMap1:
                                    floor = 1
                                    player.rect.y = 0
                                if inMap2:
                                    floor = 1
                                    player.rect.y = 0
                                if inMap3:
                                    pass
                                pass


if __name__ == "__main__":
    main()