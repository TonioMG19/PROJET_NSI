import pygame

file = "map.txt"

myListe = []

def loadMap(file):
    with open(file,"r") as map:
        for i in map:
            i = i.replace('\n','')
            myListe.append(i)
        return myListe



def drawMap(file,window,brick_o,brick_x,ladder,door):
    map = file
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'x':
                window.blit(brick_x,(j*64,i*64))
            elif map[i][j] == 'o':
                pass
                #window.blit(brick_o,(j * 64, i * 64))
            elif map[i][j] == '#':
                window.blit(ladder, (j * 64, i * 64))
            elif map[i][j] == 'p':
                window.blit(door, (j * 64, i * 64))