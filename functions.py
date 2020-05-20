import pygame

file = "map.txt"

def loadMap(file):
    with open(file,"r") as map:
        myListe = []
        for i in map:
            i = i.replace('\n','')
            myListe.append(i)
        return myListe

def drawMap(file,window,brick_o,brick_x):
    map = loadMap(file)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'x':
                window.blit(brick_x,(j*64,i*64))
            elif map[i][j] == 'o':
                window.blit(brick_o,(j * 64, i * 64))