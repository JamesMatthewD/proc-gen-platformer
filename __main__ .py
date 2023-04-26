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

FPS=60  #Screen setup


framePerSec=pygame.time.Clock()  #will be used for tracking FPS to detect issues when testing

PLAYER=classes.Player(5, 0, 0, 3, 75, 95)
allSprites=pygame.sprite.Group()
allSprites.add(PLAYER)
blocks=pygame.sprite.Group()
enemies=pygame.sprite.Group()

controls=[[0, 'left', False],  #From left to right the values are the key (for pygame), what it represents and if it is held or not
          [0, 'right', False],
          [0, 'jump', False],
          [0, 'attack', False],
          [0, 'specialAttack', False]]  #Will hopefully be editable but these will be the controls for the player

myFile=open('controls.txt', 'r')
control=0
for eachLine in myFile:
    controls[control][0]=int(eachLine.strip('\n'))  #This changes the controls to the ones specified in the controls text file, the stripping of the line is to remove the new line part of the text
    control+=1 

#print(controls)


def screenUpdate():
    for eachSprite in allSprites:
        try:
            screen.blit(eachSprite.surf, eachSprite.rect)
            if eachSprite.type==1:
                eachSprite.pathfind(PLAYER,ACC,FRIC,blocks,eachSprite, level.level)
            eachSprite.update(allSprites, eachSprite)
        except:
            pass


    time.sleep(1/FPS)

    

def playerMove(moveType, SELF):
    PLAYER.move(ACC, FRIC,  blocks, SELF, moveType)

level=classes.Level()

def levelBlit():
    level.generate()

    #for eachRow in level.level:
        #print(eachRow)

    row=0.5
    perRow=HEIGHT/len(level.level)
    for eachRow in level.level:
        perCol=WIDTH/len(eachRow)
        col=0.5  #I set row and col to 0.5 as when they were 0 or 1, the level did not show correctly with it being partially off screen
        
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
                PLAYER.pos=vec((col*perCol), (row*perRow))  #I move the player here as opposed to creating a new object as I want the health to carry over.
                PLAYER.rect=PLAYER.surf.get_rect(center=(PLAYER.pos.x, PLAYER.pos.y))

            col+=1
        row+=1

levelBlit()

while True:  #Game Loop

    moved=False

    for event in pygame.event.get():  #Detects inputs


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
                        PLAYER.cancelJump()  #This extra bit cancels the players jump if the jump key is released


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
