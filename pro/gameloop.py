import pygame
import math
import random
import sys
from pygame.locals import *

black = (0, 0, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

pygame.init()
from car_selection import carselection
from timer import*
from helper import button,text_objects

def check_collision(maincarX, maincarY, maincar_width, maincar_height, carX, carY, car_width, car_height):
    maincar_rect = pygame.Rect(maincarX, maincarY, maincar_width, maincar_height)
    car_rect = pygame.Rect(carX, carY, car_width, car_height)
    return maincar_rect.colliderect(car_rect)

def gamel_oop():
    global p,c,start_time,screen
    

    #setting background image
    bg = pygame.image.load('track2.jpg')
    track_y = 0
    scroll_speed = 5 
    # setting our player
    mc=carselection()
    maincar=pygame.image.load(mc)
    maincarX = 350
    maincarY = 495
    maincarX_change = 0
    maincarY_change = 0

    #other cars
    car1 = pygame.image.load('car1.png')
    car1X = random.randint(50,200)
    car1Y = 100

    car2 = pygame.image.load('car2.png')
    car2X = random.randint(650,800)
    car2Y = 100

    car3 = pygame.image.load('car3.png')
    car3X = random.randint(650,800)
    car3Y = 100

    coin=pygame.image.load('coin.png')
    cX=random.randint(50,800)
    cY=100
    
    maincar_width = maincar.get_width()
    maincar_height = maincar.get_height()
    car_width1= car1.get_width()
    car_height1 = car1.get_height()
    car_width2= car2.get_width()
    car_height2 = car2.get_height()
    car_width3= car3.get_width()
    car_height3 = car3.get_height()
    c_width= coin.get_width()
    c_height = coin.get_height()


   
    run = True
    gamewin=False
    start_time=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    p=True
            if p:
                screen.fill((255, 255, 255))  # Fill the screen with white color
                text = pygame.font.SysFont('ComicSans.ttf', 115)
                text_surface, text_rect = text_objects('Game Paused', text)
                text_rect.center = (400, 100)
                screen.blit(text_surface, text_rect)
                button('Continue', 100, 350, 100, 50, bright_green, bright_green, unpause)
                button('Quit', 600, 350, 100, 50, bright_red, bright_red, quit_game)
                pygame.display.flip()
                pygame.time.delay(100)
                continue

            if not p:    #checking if any key has been pressed
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        maincarX_change += 5
            
                    if event.key == pygame.K_LEFT:
                        maincarX_change -= 5
                
                    if event.key == pygame.K_UP:
                        maincarY_change -= 5
                    
                    if event.key == pygame.K_DOWN:
                        maincarY_change += 5
      
                #checking if key has been lifted up
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_RIGHT:
                        maincarX_change = 0
            
                    if event.key == pygame.K_LEFT:
                        maincarX_change = 0
                
                    if event.key == pygame.K_UP:
                        maincarY_change = 0
                    
                    if event.key == pygame.K_DOWN:
                        maincarY_change = 0            
        pygame.display.update()
        #setting boundary for our main car
        if maincarX < 0:
            maincarX = 0
        if maincarX > 798:
            maincarX = 798
        
        if maincarY < 0:
            maincarY = 0
        if maincarY > 700:
            maincarY = 700

        track_y -= scroll_speed

        track_y -= scroll_speed
        if track_y<=-bg.get_height():
            track_y=0
        
        #CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE 
        screen.fill((0,0,0))

        #displaying the background image
        screen.blit(bg,(0,track_y))
        screen.blit(bg,(0,track_y+bg.get_height()))

        #displaying our main car
        screen.blit(maincar,(maincarX,maincarY))

        #displaing other cars
        screen.blit(car1,(car1X,car1Y))
        screen.blit(car2,(car2X,car2Y))
        screen.blit(car3,(car3X,car3Y))
        screen.blit(coin,(cX,cY))
        
        #updating the values
        maincarX += maincarX_change
        maincarY +=maincarY_change

        #movement of the enemies
        car1Y += 5
        car2Y += 7
        car3Y += 10
        cY+=10


        #moving enemies infinitely
        if car1Y > 670:
            car1Y = -100
        if car2Y > 670:
            car2Y = -150
        if car3Y > 670:
            car3Y = -200
        if cY>670:
            cY=-250
           
        
        # Check collision with other cars
        

        # Check collision with other cars
        if check_collision(maincarX, maincarY, maincar_width, maincar_height, car1X, car1Y, car_width1, car_height1) or \
           check_collision(maincarX, maincarY, maincar_width, maincar_height, car2X, car2Y, car_width2, car_height2) or \
           check_collision(maincarX, maincarY, maincar_width, maincar_height, car3X, car3Y, car_width3, car_height3):
            run = False
            game_over()
            break
        if check_collision(maincarX,maincarY,maincar_width,maincar_height,cX,cY,c_width,c_height):
            c+=20
        elapsed_time = get_elapsed_time()
        if elapsed_time >= 60000:  # 1 minute (60,000 milliseconds)
            run = False
            gamewin=True
            break
        
        if gamewin==True:
            game_win()
            continue

def unpause():
    global p
    p=False
def quit_game():
    pygame.quit()

def help():
    screen.fill((255, 255, 255))
    text = pygame.font.SysFont('ComicSans.ttf', 30)
    text_surface1, text_rect1 = text_objects('''press right arrow and left arrow to move the car right and left respectively''', text)
    text_rect1.center = (400, 100)
    text_surface2, text_rect2 = text_objects('''press up and down arrows to move the car forward and backward respectively''', text)
    text_rect2.center = (400, 200)
    text_surface3, text_rect3 = text_objects('''press p to pause the game''', text)
    text_rect3.center = (400, 300)
    text_surface4, text_rect4 = text_objects('''collect coin''', text)
    text_rect4.center = (400, 400)
    text_surface1, text_rect1 = text_objects('''you'll lose the game if you collide with other cars ''', text)
    text_rect1.center = (400, 500)
    screen.blit(text_surface1, text_rect1)
    screen.blit(text_surface2, text_rect2)
    screen.blit(text_surface3, text_rect3)
    screen.blit(text_surface4, text_rect4)
    pygame.display.update()
    clock.tick(20)

def game_win():
    global p,clock,c,black,bright_green,bright_red
    p = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))  # Fill the screen with white color
        text = pygame.font.SysFont('ComicSans.ttf', 115)
        text_surface, text_rect = text_objects('You won!'+'\n'+str(c), text)
        text_rect.center = (400, 100)
        screen.blit(text_surface, text_rect)
        button('play again', 100, 350, 100, 50, bright_green, bright_green,gamel_oop)
        button('Quit', 600, 350, 100, 50, bright_red, bright_red,quit_game)
        pygame.display.update()
        clock.tick(20)

def game_over():
    global p,c
    p = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fill the screen with white color
        text = pygame.font.SysFont('ComicsSans.ttf', 115)
        text_surface, text_rect = text_objects('crashed' +'\n'+ str(c), text)
        text_rect.center = (400, 100)
        screen.blit(text_surface, text_rect)
        button('Retry', 100, 350, 100, 50, bright_green, bright_green, gamel_oop)
        button('Quit', 600, 350, 100, 50, bright_red, bright_red, quit_game)
        pygame.display.update()
        clock.tick(20)

def intro():
    global screen
    bg=pygame.image.load('background 2.png')
    screen.blit(bg,(0,0))
    button('play', 100, 350, 100, 50, bright_green,black,gamel_oop)
    button('help', 600, 350, 100, 50, bright_red, black, help)
    pygame.display.update()
