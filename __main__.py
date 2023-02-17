import pygame
from pygame import *
import classes, random, os, sys, time
vec=pygame.math.Vector2

pygame.init()  #Pygame Initialisation

WIDTH=1600
HEIGHT=900
screen=pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('wow amazing code')
ACC=1.5
FRIC=-0.12

FPS=90  #Screen setup

framePerSec=pygame.time.Clock()  #will be used for tracking FPS to detect issues when testing

PLAYER=classes.Player(5, 0, 0, 3, 75, 95)
allSprites=pygame.sprite.Group()
allSprites.add(PLAYER)
blocks=pygame.sprite.Group()
enemies=pygame.sprite.Group()

controls=[[276, 'left', False],  #From left to right the values are the key (for pygame), what it represents and if it is held or not
          [275, 'right', False],
          [273, 'jump', False],
          [122, 'attack', False],
          [120, 'specialAttack', False]]  #Will hopefully be editable but these will be the controls for the player


def screenUpdate():
    for eachSprite in allSprites:
        try:
            screen.blit(eachSprite.surf, eachSprite.rect)
            eachSprite.update(allSprites, eachSprite)
        except:
            pass


    #time.sleep(0.1)

    

def playerMove(moveType, SELF):
    PLAYER.move(ACC, FRIC,  blocks, SELF, 'moveType')


def levelBlit():
    level=classes.Level()
    level.generate()

    #for eachRow in level.level:
        #print(eachRow)

    row=0.5
    perRow=HEIGHT/len(level.level)
    for eachRow in level.level:
        perCol=WIDTH/len(eachRow)
        col=0.5
        
        for eachCol in eachRow:
            if eachCol == 'b' or eachCol == 1:
                sprite=classes.Wall((col*perCol), (row*perRow), perCol, perRow)
                blocks.add(sprite)
                allSprites.add(sprite)

            elif eachCol == 2:
                    sprite=classes.Enemy(5, (col*perCol), ((row*perRow)), 5, 60, 100)
                    enemies.add(sprite)
                    allSprites.add(sprite)

            elif eachCol == 'p':
                PLAYER.pos=vec((col*perCol), (row*perRow))
                PLAYER.rect=PLAYER.surf.get_rect(center=(PLAYER.pos.x, PLAYER.pos.y))

            col+=1
        row+=1

levelBlit()

while True:  #Game Loop

    moved=False

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

        if event.type==pygame.KEYDOWN:
            for eachKey in controls:
                if eachKey[0]==event.key:
                    PLAYER.move(ACC, FRIC, blocks, PLAYER, eachKey[1])
                    moved=True
                    eachKey[2]=True


        if event.type==pygame.KEYUP:
            for eachKey in controls:
                if eachKey[0]==event.key:
                    eachKey[2]=False

                    if eachKey[1]=='jump':
                        PLAYER.cancelJump()


        for eachKey in controls:
            if eachKey[2]==True:
                PLAYER.move(ACC, FRIC, blocks, PLAYER, eachKey[1])

    if moved!=True:
            PLAYER.move(ACC, FRIC, blocks, PLAYER)
            
            
    screen.fill((255,255,255))  #Testing purposes only
        #Check for inputs here, if one is recieved then call the move method [PLAYER.super().move(move type)], move will be called from the enemy pathfind method.

    screenUpdate()  #Subprogram to update the positions of all sprites and display them

    pygame.display.update()
    framePerSec.tick(FPS)
