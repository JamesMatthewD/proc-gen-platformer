import pygame
from pygame.locals import *
import python
pygame.init()
vec=pygame.math.Vector2

class MovingEntity(pygame.sprite.Sprite):

    def __init__(self, health, posX, posY, damageNum, typeOfEntity):

        super().__init__()
        self.pos=vec(posX, posY)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.health=health
        self.damage=damageNum

        self.jumping=False
        self.type=typeOfEntity


    def move(self):
        if self.type==0:
            ##PLAYER
            pass
        elif self.type==1:
            ##ENEMY
            pass


    def update(self):
        ##Collisions and other stuff
        pass

    def jump(self):
        ##Process Jumping
        pass

    def cancelJump(self):
        ##if key is let go then stop upward acceleration
        pass

    def damageTaken(self):
        ##Call in update to change the health
        pass

    def animate(self):
        ##animation queue? 2D array of frames, animation part/priority/timeLeftUntilAnimate
        ##Flush queue when inerrupt like movement
        pass


class Player(MovingEntity):

    def __init__(self, health, posX, posY, damageNum):
        super().__init__(health, posX, posY, damageNum, 0)

        self.score=0
        self.battleBar=0.0

    def heal(self):
        ##HEAL PLAYER, call after update method
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
        super().__init__(health, posX, posY, damageNum, 1)

    def pathfind(self):
        ##do pathfinding algorithm etc
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
        self.level=[[],[],[],[],[],[],[],[],[]]

    def generate(self):
        for eachRow in self.level:
            pass  #Generate level 1 row at a time