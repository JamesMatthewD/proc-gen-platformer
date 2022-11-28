import pygame
from pygame import *
import classes, random, os, sys, time

pygame.init()  #Pygame Initialisation

WIDTH=1600
HEIGHT=900
screen=pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Game')
FPS=60  #Screen setup

framePerSec=pygame.time.Clock()  #will be used for tracking FPS to detect issues when testing

PLAYER=classes.Player(5, 0, 0, 3)
allSprites=pygame.sprite.Group()
allSprites.add(PLAYER)

controls={left: 'K_LEFT',
          right: 'K_RIGHT',
          jump: 'K_UP'
          attack: 'K_z',
          specialAttack: 'K_x'}  #Will hopefully be editable but these will be the controls for the player

def screenUpdate():
    for eachSprite in allSprites:
        try:
            eachSprite.update()
        except:
            pass

    pygame.display.update()
    framePerSec.tick(FPS)

while True:  #Game Loop

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
    screen.fill(255,255,255)  #Testing purposes only
        #Check for inputs here, if one is recieved then call the move method [PLAYER.super().move(move type)], move will be called from the enemy pathfind method.

    screenUpdate()  #Subprogram to update the positions of all sprites and display them
