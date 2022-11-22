import pygame
from pygame import *
import classes, random, os, sys, time

pygame.init()  #Pygame Initialisation

myFile=open('windowTitles.txt', 'r')
windowTitles=myFile.readlines()
myFile.close()
windowTitle=random.choice(windowTitles)  #Chooses a random window title

WIDTH=1600
HEIGHT=900
screen=pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(windowTitle)
FPS=60  #Screen setup

framePerSec=pygame.time.Clock()  #will be used for tracking FPS to detect issues when testing

PLAYER=classes.Player(5, 0, 0, 3)
allSprites=pygame.sprite.Group()
allSprites.add(PLAYER)

def screenUpdate():
    for eachSprite in allSprites:
        eachSprite.update()

    pygame.display.update()
    framePerSec.tick(FPS)

while True:  #Game Loop

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

    screenUpdate()  #Subprogram to update the positions of all sprites and display them