import pygame
import json

def loadMap(file):
    myListe = []
    with open(file,"r") as map:
        for i in map:
            i = i.replace('\n','')
            myListe.append(i)
        return myListe



def drawMap(file,window,brick_x,ladder,door,trappe,key, closed_trap):
    map = file
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'x':
                window.blit(brick_x,(j*64,i*64))
            elif map[i][j] == '#':
                window.blit(ladder, (j * 64, i * 64))
            elif map[i][j] == 'p':
                window.blit(door, (j * 64, i * 64))
            elif map[i][j] == 't':
                window.blit(trappe, (j * 64, i * 64))
            elif map[i][j] == 'k':
                window.blit(key, (j * 64, i * 64))
            elif map[i][j] == 'c':
                window.blit(closed_trap, (j * 64, i * 64))

def open_trappe(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'c':
                map[i] = map[i][:j] + 't' + map[i][j+1:]

def reset_map(map,default_map):
    map = default_map
    return map

def loadAdvance():
    with open("status.json") as out_file:
        status = json.load(out_file)
    return status

def saveAdvance(status):
    with open("status.json", "w") as out_file:
        json.dump(status, out_file)
    return 0


