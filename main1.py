import pygame
import button

pygame.init()
from pygame.locals import*
screen = pygame.display.set_mode((800,700))

#changing the title of game window
pygame.display.set_caption('Adrenaline Rush')

#change the logo
logo = pygame.image.load('carlogo.jpeg')
pygame.display.set_icon(logo)

#setting background image
background = pygame.image.load('background.jpeg')
screen.blit(background,(0,0))
pygame.display.update()


#load button images
play_img =pygame.image.load('button_play.jpg').convert_alpha()
help_img = pygame.image.load('button_help.jpg').convert_alpha()

#create button instances
play_button = button.Button(550,100, play_img, 0.8)
help_button = button.Button(550,300, help_img, 0.8)

run = True
while run:
    if play_button.draw(screen):
         print('PLAY')
    if help_button.draw(screen):
         print('HELP')
    
    #event handler
    for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
               run = False

#diasplay the background image
        
    pygame.display.update()
pygame.quit()