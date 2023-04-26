import pygame
from pygame.locals import *
import random
import pathfind

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


    def move(self, ACC, FRIC, blockGroup, SELF, moveType=None):

        self.acc=vec(0,0.32)  #This is the constant for gravity so that at the start of every movement frame, the player starts falling.
        
        if moveType=='left' or moveType=='right':
            
            if moveType=='left':
                self.acc.x-=ACC
            else:
                #If its not left movement it will be right movement
                self.acc.x+=ACC

        self.acc.x+=self.vel.x * FRIC
        self.vel+=self.acc  #This updates the velocity with the acceleration calculated

        self.pos.y+=self.vel.y+0.5*self.acc.y  #This updates the y position of the player

        self.pos.x+=self.vel.x+0.5*self.acc.x #This updates the x position of the player
        

        self.checkCollisions(blockGroup, SELF)  #Performs collision checks and acts on them

        self.rect=self.surf.get_rect(center=(self.pos.x, self.pos.y))  #This updates where the rectangle shown is located on the screen.
                
        if moveType=='jump':
            ##Call jump method//continue jump
            if self.jumping==False:
                self.jump(blockGroup)

            '''    
            if self.jumping==True:
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if pygame.K_UP not in pygame.KEYDOWN:
                            self.cancelJump()
            '''
                
        elif moveType=='attack':
            ##Proccess standard attack
            pass
        elif moveType=='specialAttack':
            ##Proccess the special attack, wouldn't be called by enemies
            pass


    def checkCollisions(self, otherGroup, SELF):
        
        collisions=pygame.sprite.spritecollide(SELF, otherGroup, False)  #This is the pygame built in function to check for sprite collisions
        for eachSprite in collisions:

            #print("est: ", eachSprite.type, "st: ", SELF.type)

            if eachSprite.type==2 and (SELF.type==1 or SELF.type==0) and eachSprite.type!=SELF.type:
            #This is extra validation to make sure the correct collisions is applied to the sprite

                #print("enemy or player attempting to collide with wall")

                #print(SELF.pos.x, SELF.pos.y, eachSprite.pos.x, eachSprite.pos.y)
                '''

                pushBack=-SELF.vel.x
                SELF.pos.x-=pushBack

                self.vel.x=0


                if SELF.pos.y>eachSprite.pos.y:
                    SELF.pos.y=eachSprite.rect.bottom+47
                    
                else:
                    SELF.pos.y=eachSprite.rect.top-47
                    SELF.vel.y=0
                    SELF.jumping=False   


                hits=pygame.sprite.spritecollide(SELF, otherGroup, False)
                if hits and recursions<10:
                    SELF.checkCollisions(otherGroup, SELF, recursions+1)
                    break


                hits=pygame.sprite.spritecollide(SELF, otherGroup, False)

                if hits:
                    difference=SELF.pos-eachSprite.pos

                    if SELF.vel.x!=0:

                        if difference.x<0:
                            SELF.pos.x=eachSprite.rect.right+47
                        else:
                            SELF.pos.x=eachSprite.rect.left-47

                    if difference.y<0:
                        SELF.pos.y=eachSprite.rect.top-47
                    else:
                        SELF.pos.y=eachSprite.rect.bottom+47
                '''

            
                '''
                yDiff=SELF.pos.y-eachSprite.pos.y
                xDiff=SELF.pos.x-eachSprite.pos.x

                if abs(xDiff) > abs(yDiff):
                    SELF.pos.x-=xDiff

                elif abs(xDiff) < abs(yDiff):
                    
                    if yDiff>0:
                        SELF.pos.y+=SELF.vel.y
                        SELF.jumping=False
                        SELF.vel.y=0

                    else:
                        SELF.pos.y-=SELF.vel.y

            
                ##Old system which didnt work           
                if SELF.pos.x > eachSprite.pos.x:
                    #pushBack=(-SELF.vel.x)
                    print("p>b")
                    SELF.pos.x=eachSprite.rect.right+40

                elif SELF.pos.x < eachSprite.pos.x:
                    #pushBack=SELF.vel.x
                    print("p<b")
                    SELF.pos.x=eachSprite.rect.left-40

                else:
                    print("pos x are same")

                if SELF.pos.y > eachSprite.pos.y:
                    #pushBack=SELF.vel.y
                    SELF.vel.y=0
                    print("p>b")
                    SELF.pos.y=eachSprite.rect.bottom+50

                elif SELF.pos.y < eachSpirte.pos.y:
                    #pushBack=-SELF.vel.y
                    print("p<b")
                    SELF.vel.y=0
                    SELF.jumping=False
                    SELF.pos.y=eachSprite.rect.top-50
                
                ##pushback attempt 1
                print(pushBack)
                SELF.pos-=pushBack
                print(SELF.pos)
                '''

                ##find edge of block and entity, then compare and put entity in correct place relative
                blockEdges=[]  #I add each of the edges for the block into an array
                blockEdges.append(eachSprite.rect.top)
                blockEdges.append(eachSprite.rect.bottom)
                blockEdges.append(eachSprite.rect.right)
                blockEdges.append(eachSprite.rect.left)
                
                entityEdges=[]  #I do the same for the entity thats moving
                entityEdges.append(SELF.rect.top)
                entityEdges.append(SELF.rect.bottom)
                entityEdges.append(SELF.rect.right)
                entityEdges.append(SELF.rect.left)

                #perform collision check here, check vel and if moving in direction then compare the respective ones. y first
                '''
                if SELF.vel.y>0:
                    if entityEdges[1]>blockEdges[0]:
                        SELF.pos.y=blockEdges[0]-48
                        SELF.vel.y=0
                        SELF.jumping=False
                        yMoved=True

                elif SELF.vel.y<0:
                    if entityEdges[0]<blockEdges[1]:
                        SELF.pos.y=blockEdges[1]+48
                        SELF.vel.y=0
                        yMoved=True

                if SELF.vel.x>0:
                    if entityEdges[2]>blockEdges[3]:
                        SELF.pos.x=blockEdges[2]+45
                        SELF.vel.x=0
                        xMoved=True

                elif SELF.vel.x<0:
                    if entityEdges[3]<blockEdges[2]:
                        SELF.pos.x=blockEdges[3]-45
                        SELF.vel.x=0
                        xMoved=True
            '''
            #check vel of player, then check where its colliding. then if in air/non 0 y then maintain it but keep x out of block

            rightDiff=entityEdges[3]-blockEdges[2]  #Compares left of the entity with the right of the block
            leftDiff=entityEdges[2]-blockEdges[3]  #Compares right of entity with left of block

            
            topDiff=entityEdges[1]-blockEdges[0]  #Compares bottom of entity with top of block
            bottomDiff=entityEdges[0]-blockEdges[1]  #Compares top of entity with bottom of block
            #If the player is above the block then the topDiff will be negative, but if the player is below the block then bottomDiff will be positive
            #if the player is colliding on the top of the block then topDiff will be positive, bottomDiff wil be negative


            if topDiff>bottomDiff and self.pos.y<eachSprite.pos.y:
                mostY=abs(topDiff)
            else:
                mostY=abs(bottomDiff)
                #print("bottom diff")

            if rightDiff<leftDiff and self.pos.x<eachSprite.pos.x:
                mostX=abs(leftDiff)
            else:
                mostX=abs(rightDiff)


            if mostX<mostY:
                ##do x collisions
                if leftDiff>0 and self.pos.x<eachSprite.pos.x:
                    SELF.pos.x=blockEdges[3]-38
                    #self.pos.x-=rightDiff
                    SELF.vel.x=0

                else:
                    SELF.pos.x=blockEdges[2]+38
                    #self.pos.x+=leftDiff
                    SELF.vel.x=0

##                hits=pygame.sprite.spritecollide(SELF, otherGroup, False)
##                if hits:
##                    if topDiff>0 and SELF.pos.y<eachSprite.pos.y:
##                        #SELF.pos.y=blockEdges[0]-48
##                        self.pos.y-=topDiff
##                        SELF.jumping=False
##                        SELF.vel.y=0
##                        break
##
##                else:
##                    #SELF.pos.y=blockEdges[1]+48
##                    self.pos.y+=bottomDiff
##                    self.vel.y=0

            else:
                #print("vertical colissions")
                if topDiff>0 and SELF.pos.y<eachSprite.pos.y:
                    SELF.pos.y=blockEdges[0]-48
                    #self.pos.y-=topDiff
                    SELF.jumping=False
                    SELF.vel.y=0
                    break

                else:
                    SELF.pos.y=blockEdges[1]+48
                    #print("sent to the bottom")
                    #self.pos.y+=bottomDiff

##                hits=pygame.sprite.spritecollide(SELF, otherGroup, False)
##                if hits:
##                    if leftDiff>0 and rightDiff<0:
##                        #SELF.pos.x=blockEdges[3]-38
##                        self.pos.x-=rightDiff
##                        SELF.vel.x=0
##                    else:
##                        #SELF.pos.x=blockEdges[2]+38
##                        self.pos.x+=leftDiff
##                        SELF.vel.x=0
                                    


    def jump(self, blockGroup):
        ##Process Jumping
             
        if self.jumping==False:
            self.vel.y=-13
            self.jumping=True

    def cancelJump(self):
        ##if key is let go then stop upward acceleration
        if self.jumping:
            if self.vel.y<-3:
                self.vel.y=-3

    def damageTaken(self, damageNumber):
        ##Call in update to change the health
        pass

    def animate(self):
        ##animation queue? 2D array of frames, animation part/priority/timeLeftUntilAnimate
        ##Flush queue when inerrupt like movement
        pass


class Player(MovingEntity):

    def __init__(self, health, posX, posY, damageNum, width, height):
        super().__init__(health, posX, posY, damageNum)

        self.type=0

        self.score=0
        self.battleBar=0.0

        self.surf=pygame.Surface((width,height))
        self.rect=self.surf.get_rect(center=(self.pos.x, self.pos.y))

        
        self.surf.fill((0,0,255))

    def update(self, otherGroup, SELF):
        super().checkCollisions(otherGroup, SELF)
        #Would then perform actions based on the collisions
        #Would also add next frame to animation queue.

    def move(self, ACC, FRIC, blockGroup, SELF, moveType=None):
        super().move(ACC, FRIC, blockGroup, SELF, moveType)
        
    def heal(self):
        ##HEAL PLAYER, call after update method
        super().damageTaken() #Use negative number for the parameter, negative damage = heal
        pass

    def cancelJump(self):
        super().cancelJump()

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

    def __init__(self, health, posX, posY, damageNum, width, height):
        super().__init__(health, posX, posY, damageNum)
        self.type=1
        self.surf=pygame.Surface((width,height))
        self.rect=self.surf.get_rect(center=(self.pos.x, self.pos.y))
        self.surf.fill((0,255,0))

        self.pathfindCooldown=35
        self.direction='left'
    
    def update(self, otherGroup, SELF):
        super().checkCollisions(otherGroup, SELF)
        ##Perform actions based on the collisions
        #If collides with the hitbox for player attack, then would call the super damage taken method.

    def pathfind(self, PLAYER, ACC, FRIC, blockGroup, level):
        ##do pathfinding algorithm and call move method
        '''Assing player to square on level and then pathfind from the enemy'''
        closestBlock=vec(int(PLAYER.pos.x/160), int(PLAYER.pos.y/(900/8)))
        currentPos=vec(int(self.pos.x/160), int(self.pos.y/(900/8)))
        path = pathfind.enemyPathfind(currentPos, closestBlock, level)

        super.move(ACC, FRIC,blockgroup, self, path[0])

        if path[1]=='jump':
            super.move(ACC, FRIC,blockgroup, self, path[1])
        



class Wall(pygame.sprite.Sprite):
    def __init__(self, posX, posY, width, height):
        super().__init__()

        self.type=2

        self.pos=vec(posX,posY)
        self.width=width
        self.height=height

        self.surf=pygame.Surface((width,height))
        self.rect=self.surf.get_rect(center=(self.pos.x, self.pos.y))
        self.surf.fill((0,0,0))


class HUD(pygame.sprite.Sprite):
    def __init__(self, posX,posY, typeOfHUD, number):
        super().__init__()

        self.type=3

        self.num=number #This can represent either the health or the score
        self.pos=vec(posX,posY)


class Level():
    def __init__(self):
        self.level=[]

        self.elements={'air': 0,
                       'block': 1,
                       'enemy': 2}  #This dictionary doesn't contain entrance and exit as they won't be changeable locations and thus wouldn't be worth including in here

        self.immutables={'air': 'a',
                         'block': 'b',
                         'enemy': 'c',
                         'entrance': 'd',
                         'exit': 'e',
                         'player': 'p'}

            
        #8 Rows of blocks, 1 row for ceiling, 1 row for floor
        #The level generation will use characters in the arrays for each row, and will generate the correct sprite/the correct object
    
    def generate(self):

        validated=False

        while validated==False:

            self.level=[]
        
            myFile=open('initialLevel.txt', 'r')
            for eachRow in myFile:
                row=[]
                chars=eachRow
                for eachChar in chars:
                    if eachChar!='\n':
                        row.append(eachChar)

                self.level.append(row)

            myFile.close()  #This regenerates the level as it either was not possible or is the first loop and thus needs to generate a level to be validated
            
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
                                    leftRight=random.random()  #This randomly choses a direction for the block under the enemy to generate
                                    #I chose to add this because enemies should not be trapped and surrounded by blocks so there needs to be at least one block of movement available
                                    if leftRight>0.5:
                                        self.level[row+1][col-1]=self.immutables['block']
                                        self.level[row][col-1]=self.immutables['air']
                                        
                                    else:
                                        self.level[row+1][col+1]=self.immutables['block']
                                        self.level[row][col+1]=self.immutables['air']

                        elif chosenElement>0.75:
                            self.level[row][col]=self.elements['block']

                        else:
                            self.level[row][col]=self.elements['air']

                        col=col+1
                    except:
                        col+=1
                row+=1


             ##Entrance exit generation
            entranceLocation=random.randint(1,6)
            exitLocation=random.randint(1,6)
            self.level[entranceLocation][0]=self.immutables['entrance']
            self.level[entranceLocation+1][1]=self.immutables['block']
            self.level[entranceLocation][1]=self.immutables['player']
            self.level[exitLocation][9]=self.immutables['exit']
            self.level[exitLocation+1][8]=self.immutables['block']  #There is a block next to the entrance and exit so that the player can enter them easily
            self.level[exitLocation][8]=self.immutables['air'] #There is air next to the entrance and exit so that they aren't blocked off

            for eachRow in self.level:
                print(eachRow)

            print('\n')

            exitCoord=tuple((9, exitLocation))

            '''validated=True'''
            
            #self.level=[[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]]

            if pathfind.pathfind(exitCoord, tuple((1, entranceLocation)), self.level)!=False:
                validated=True  #This updates the while condition so that if a path is found then the level is passed through to the blitting stage
            


##Debugging/Testing
'''level=Level()
level.generate()
for eachRow in level.level:
    print(eachRow)'''
