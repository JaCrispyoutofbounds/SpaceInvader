import random
import math
import pygame
from pygame.constants import KEYDOWN
from pygame import mixer

#initializing th module
pygame.init()

# initializing the screen
screen=pygame.display.set_mode((800,600))
icon=pygame.image.load('SpaceInvader\space.png')
pygame.display.set_icon(icon)

# background
background=pygame.image.load("SpaceInvader\ground.jpg")

# bg Sound
# mixer.music.load("D:\Python\SpaceInvader\music.wav")
# mixer.music.play(-1)


# player
playerimg=pygame.image.load("SpaceInvader\space2.png")
playerx=370
playery=480
playerch=0

# score
score=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10

# game over text

gofont=pygame.font.Font('freesansbold.ttf',64)

def gameovertext():
    gotext=font.render('GAME OVER '+str(score),True,(225,225,225))
    screen.blit(gotext,(200,250))

def showscore(x,y):
    score_value = gofont.render('Score : '+str(score),True,(225,225,225))
    screen.blit(score_value,(x,y))

def player(x,y):
    screen.blit(playerimg,(x,y))

# enemy

enemyimg=[]
enemyx=[]
enemyy=[]
enemyxch=[]
enemyych=[]

numofenemy=6
for i in range(numofenemy):

    enemyimg.append(pygame.image.load("SpaceInvader\enemy.png"))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    enemyxch.append(0.3)
    enemyych.append(40)




def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))


# bullet

# ready-cant be seen on screen
# fire-can be seen 
bulletstate="ready"

bullet=pygame.image.load("SpaceInvader\Projectile.png")
bulletx=0
bullety=480
bulletxch=2
bulletych=2

def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bullet,(x+16,y+10))

#Title and icon
pygame.display.set_caption("A game")

# collision
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2)+(math.pow(enemyy-bullety,2)))
    if distance<27:
        return True
    else:
        return False



# gameloop
running=True
while running:
    #RGB Values for bg
    screen.fill((0,0,0))
    # backgrougn image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    # checking if the key is right or left

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerch=-0.5
                
            if event.key==pygame.K_RIGHT:
                playerch=+0.5
            
            if event.key==pygame.K_SPACE:
                if bulletstate=="ready":
                    bulletx=playerx
                    firebullet(bulletx,bullety)
                    bulletsound=mixer.Sound("SpaceInvader\laser.wav")
                    bulletsound.play()

            
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                playerch=0
                


    playerx+=playerch
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736


    for i in range (numofenemy):
        if enemyy[i]>440:
            for j in range(numofenemy):
                enemyy[j]=2000
            gameovertext()
            break

        enemyx[i]+=enemyxch[i]
        if enemyx[i]<=0:
            enemyxch[i]=0.3
            enemyy[i]+=enemyych[i]
        elif enemyx[i]>=736:
            enemyxch[i]=-0.3
            enemyy[i]+=enemyych[i]

    
    # collision
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            bullety=480
            bulletstate="ready"
            score+=1
            exploisonsound=mixer.Sound("SpaceInvader\explosion.wav")
            exploisonsound.play()
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150)
            
        
        enemy(enemyx[i],enemyy[i],i)

    # bullet movement
    if bullety<=0:
        bullety=480
        bulletstate="ready"
    if bulletstate=="fire":
        firebullet(bulletx,bullety)
        bullety-=bulletych

    showscore(textX,textY)
    player(playerx,playery)
    pygame.display.update()



