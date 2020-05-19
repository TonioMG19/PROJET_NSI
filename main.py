import pygame
import random
import math
import os
import time

pygame.init()
pygame.font.init()

def main():

    window = pygame.display.set_mode((800, 800))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()