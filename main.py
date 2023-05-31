import pygame
pygame.init()
import math
import random
from pygame.locals import *
screen=pygame.display.set_mode((800,700))
pygame.display.set_caption('ADRENALINE RUSH')
logo=pygame.image.load('logo.png')
pygame.display.set_icon(logo)
black = (0, 0, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
p=False
clock=pygame.time.Clock

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[0]>y:
          pygame.draw.rect(screen,ac,(x,y,w,h))
          if click[0]==1 and action!=None:
               action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    t=pygame.font.SysFont('ComicSans',20)
    ts,tr=text_objects(msg,t)
    tr.center=(x+w/2,y+h/2)
    screen.blit(ts,tr)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def carselection():
    backg=pygame.image.load('background 2.png')
    caropts=[car1,car2,car3]
    car_rects=[]
    for i,car in enumerate(caropts):
        car_rect=car.get_rect()
        car_rect.center=(200+i*200,300)
        car_rects.append(car_rect)
    selected_car=None
    selecting=True
    while selecting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                for i ,car_rect in enumerate(car_rects):
                    if car_rect.collidepoint(mouse_pos):
                        selected_car=car_rect
                        n=i
                        selecting=False

def generaterandomcars():
    car_images=[(car1,1),(car2,2),(car3,3)]
    random_cars=[]
    for i in range(3):
        car=random.choice(car_images)
        random_cars.append(car)
    return random_cars
def gencoins():
    cs=[(c1,1),(c2,2)]
    rc=[]
    for i in range(2):
        c=random.choice(cs)
        rc.append(c)
    return rc
def gameloop():
    global c
    global p
    backg=pygame.image.load(background)
    maincar,n=carselection()
    maincarx=400
    maincary=350
    maincarxch=0
    maincarych=0
    ocars=generaterandomcars()
    car1=ocars[0][1]
    tcar1=ocars[0][0]
    car2=ocars[1][1]
    tcar2=ocars[1][0]
    car3=ocars[2][1]
    tcar4=ocars[2][0]
    coins=gencoins()
    c1=coins[0][1]
    c1v=coins[0][0]
    c2=coins[1][1]
    c2v=coins[1][0]
    car1x=random.randint(300,600)
    car1y=150
    car2x=random.randint(300,500)
    car2y=150
    car3x=random.randint()
    car3y=150
    c1x=random.randint(300,600)
    c1y=100
    c2x=random.randint(300,600)
    c2y=100

    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    p=True
        if not p:
            for event in pygame.event.get():
                if event.key==pygame.K_RIGHT:
                    maincarxch+=5
                if event.key==pygame.K_LEFT:
                    maincarxch-=5
                if event.key==pygame.K_UP:
                    if n==1:
                        maincarych+=2
                    if n==2:
                        maincarych+=4
                    if n==3:
                        maincarych+=5
                if event.key==pygame.K_DOWN:
                    maincarych-=3
        if maincarx<300:
            maincarx=300
        if maincarx>600:
            maincarx=600
        if maincary<0:
            maincary=0
        if maincary>600:
            maincary=600
    def collision(cx,cy,mcx,mcy):
        d=math.sqrt(math.pow(cx-mcx,2)+math.pow(cy-mcy,2))
        if d<50:
            return True
        else:
            return False
    coll1=collision(car1x,car1y,maincarx,maincary)
    coll2=collision(car2x,car2y,maincarx,maincary)
    coll3=collision(car3x,car3y,maincarx,maincary)
    ccoll1=collision(c1x,c1y,maincarx,maincary)
    ccoll2=collision(c2x,c2y,maincarx,maincary)
    if ccoll1:
        c+=10
    if ccoll2:
        c+=20
    if coll1 or coll2 or coll3:
        gameover()
    screen.blit(backg,(0,0))
    screen.blit(maincar,(maincarx,maincary))
    screen.blit(car1,(car1x,car1y))
    screen.blit(car2,(car2x,car2y))
    screen.blit(car3,(car3x,car3y))
    pygame.display.update()


def paused():
    t=pygame.font.SysFont('ComicSans',115)
    ts,tr=text_objects('game paused',t)
    tr.center=((400),(350))
    screen.blit(ts,tr)
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
    button('CONTINUE',100,350,50,50,bright_green,black,unpause)  
    button('quit',500,350,50,50,bright_red,black,quit_game)
    pygame.display.update()
    clock.tick(20)  

def unpause():
    global p
    p=False
def quit_game():
    pygame.quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if paused:
        screen.fill((255, 255, 255))  # Fill the screen with white color
        text = pygame.font.SysFont('Comicsansms', 115)
        text_surface, text_rect = text_objects('Game Paused', text)
        text_rect.center = (400, 350)
        screen.blit(text_surface, text_rect)
        button('Continue', 100, 350, 100, 50, bright_green, bright_green, unpause)
        button('Quit', 600, 350, 100, 50, bright_red, bright_red, quit_game)
        pygame.display.update()
        clock.tick(20)
    else:
        introduction()




    



   












    


          

    
     
     
    




