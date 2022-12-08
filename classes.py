import pygame
from pygame.locals import *
import random
pygame.init()
vec=pygame.math.Vector2

class MovingEntity(pygame.sprite.Sprite):

    def __init__(self, health, posX, posY, damageNum):

        super().__init__()
        self.pos=vec(posX, posY)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.health=health
        self.damage=damageNum

        self.jumping=False


    def move(self, moveType):
        if moveType=='Left':
            ##Process left movement
            pass
        elif moveType=='Right':
            ##Process right movement
            pass
        elif moveType=='Jump':
            ##Call jump method//continue jump
            pass
        elif moveType=='Attack':
            ##Proccess standard attack
            pass
        elif moveType=='Special Attack':
            ##Proccess the special attack, wouldn't be called by enemies
            pass
        else:
            ##Stop acceleration or jump and check colissions
            pass


    def checkCollisions(self, objectGroup, otherGroup):
        ##Checks the collisions
        pass

    def jump(self):
        ##Process Jumping
        pass

    def cancelJump(self):
        ##if key is let go then stop upward acceleration
        pass

    def damageTaken(self, damageNumber):
        ##Call in update to change the health
        pass

    def animate(self):
        ##animation queue? 2D array of frames, animation part/priority/timeLeftUntilAnimate
        ##Flush queue when inerrupt like movement
        pass


class Player(MovingEntity):

    def __init__(self, health, posX, posY, damageNum):
        super().__init__(health, posX, posY, damageNum)

        self.score=0
        self.battleBar=0.0

    def update(self, objectGroup, otherGroup):
        super().checkCollisions(objectGroup, otherGroup)
        pass
        #Would then perform actions based on the collisions
        #Would also add next frame to animation queue.
        
    def heal(self):
        ##HEAL PLAYER, call after update method
        super().damageTaken() #Use negative number for the parameter, negative damage = heal
        pass

    def getAttackType(self):
        ##call when attack key pressed, get the type of attack to perform
        pass

    def attack(self):
        ##CALL getAttackType, then queue animations and stuff
        pass

    def battleBarUpdate(self):
        ##only increase if not full, fill up a bit with attacking or killing
        pass

    def specialAttack(self):
        ##if input first check battle bar then reduce it by certain amount. then queue the animations etc
        pass



class Enemy(MovingEntity):

    def __init__(self, health, posX, posY, damageNum):
        super().__init__(health, posX, posY, damageNum)
        
    
    def update(self, objectGroup, otherGroup):
        super().checkCollisions(objectGroup, otherGroup)
        pass ##Perform actions based on the collisions
        #If collides with the hitbox for player attack, then would call the super damage taken method.

    def pathfind(self):
        ##do pathfinding algorithm and call move method.
        pass


class Wall(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()

        self.pos=vec(posX,posY)


class HUD(pygame.sprite.Sprite):
    def __init__(self, posX,posY, typeOfHUD, number):
        super().__init__()

        self.num=number #This can represent either the health or the score
        self.pos=vec(posX,posY)


class Level():
    def __init__(self):
        self.level=[]
        
        myFile=open('initialLevel.txt', 'r')
        for eachRow in myFile:
            row=[]
            chars=eachRow
            for eachChar in chars:
                if eachChar!='\n':
                    row.append(eachChar)

            self.level.append(row)

        self.elements={'air': 0,
                       'block': 1,
                       'enemy': 2}  #This dictionary doesn't contain entrance and exit as they won't be changeable locations and thus wouldn't be worth including in here

        self.immutables={'air': 'a',
                         'block': 'b',
                         'enemy': 'c',
                         'entrance': 'd',
                         'exit': 'e'}

            
        #8 Rows of blocks, 1 row for ceiling, 1 row for floor, I don't currently know how many columns there will be
        #The level generation will use characters in the arrays for each row, and will generate the correct sprite/the correct object
    
    def generate(self):

        ##Entrance exit generation
        entranceLocation=random.randint(1,6)
        exitLocation=random.randint(1,6)
        self.level[entranceLocation][0]=self.immutables['entrance']
        self.level[entranceLocation+1][1]=self.immutables['block']
        self.level[entranceLocation][1]=self.immutables['air']
        self.level[exitLocation][9]=self.immutables['exit']
        self.level[exitLocation+1][8]=self.immutables['block']  #There is a block next to the entrance and exit so that the player can enter them easily
        self.level[exitLocation][8]=self.immutables['air'] #There is air next to the entrance and exit so that they aren't blocked off

        
        row=0
        for eachRow in self.level:
            col=0
            for eachCol in eachRow:
                try:
                    test=int(self.level[row][col])%1 #This makes is so that an error is caused from attempting to divide a letter so it knows to skip that block
                    if row==0 or row==7 or col==0 or col==9:
                        self.level[row][col]=self.immutables['block']  #This makes it so that borders of the level are blocks (prevents player falling out of level
                        col+=1
                        continue

                    chosenElement=random.random()  #This generates a random number that I can use to determine how to level will be generated

                    if chosenElement>0.95:
                        self.level[row][col]=self.elements['enemy']
                        
                        if row!=7:
                            self.level[row+1][col]=self.immutables['block']

                            if col==1:
                                self.level[row+1][col+1]=self.immutables['block']
                                self.level[row][col+1]=self.immutables['air']
                                
                            elif col==8:
                                self.level[row+1][col-1]=self.immutables['block']
                                self.level[row][col-1]=self.immutables['air']
                                
                            else:
                                leftRight=random.random()
                                
                                if leftRight>0.5:
                                    self.level[row+1][col-1]=self.immutables['block']
                                    self.level[row][col-1]=self.immutables['air']
                                    
                                else:
                                    self.level[row+1][col+1]=self.immutables['block']
                                    self.level[row][col+1]=self.immutables['air']

                    elif chosenElement>0.65:
                        self.level[row][col]=self.elements['block']

                    else:
                        self.level[row][col]=self.elements['air']

                    col=col+1
                except:
                    col+=1
            row+=1
            


##Debugging/Testing
level=Level()
level.generate()
for eachRow in level.level:
    print(eachRow)
