import pygame
pygame.init()

myFile=open('controls.txt', 'w')
myFile.close()

def resetText():
    key='Press New Key for ' + controls[controlReset]
    reset_text=font.render(key, 1, pygame.Color("blue"))
    return reset_text

FPS=60
framePerSec=pygame.time.Clock()
HEIGHT=500
WIDTH=500
screen=pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Reset Controls')

font=pygame.font.SysFont('Comic Sans', 18)

controlReset=0
controls=['Left', 'Right', 'Jump', 'Attack', 'Special Attack']

while True:
    
    if controlReset==5:
        pygame.quit()
        
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        
        if event.type==pygame.KEYDOWN:
            myFile=open('controls.txt', 'a')
            myFile.write(str(event.key)+'\n')  #This writes the new controls to the text file
            myFile.close()
            controlReset+=1
            pygame.display.update()
            
            
    screen.blit(resetText(), (100,(50+(40*controlReset))))
    pygame.display.update()
    framePerSec.tick(FPS)