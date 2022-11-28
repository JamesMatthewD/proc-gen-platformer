import pygame
from pygame.locals import *
import python
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
        elif moveType=='Right':
            ##Process right movement
        elif moveType=='Jump':
            ##Call jump method//continue jump
        elif moveType=='Attack':
            ##Proccess standard attack
        elif moveType=='Special Attack':
            ##Proccess the special attack, wouldn't be called by enemies
        else:
            ##Stop acceleration or jump and check colissions


    def checkCollisions(self, objectGroup, otherGroup, False):
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
        self.level=[[],[],[],[],[],[],[],[]] #8 Rows of blocks, 1 row for ceiling, 1 row for floor, I don't currently know how many columns there will be
        #The level generation will use characters in the arrays for each row, and will generate the correct sprite/the correct object

    def generate(self):
        for eachRow in self.level:
            pass  #Generate level 1 row at a time
