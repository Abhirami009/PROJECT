import pygame
import math
import random
import sys
from pygame.locals import*
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((800,700))
pygame.display.set_caption('ADRENALINE RUSH')
logo=pygame.image.load('logo.png')
pygame.display.set_icon(logo)
black = (0, 0, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
p=False
clock=pygame.time.Clock()
timer_started = False
start_time = 0
c=0



def start_timer():
    global timer_started, start_time
    timer_started = True
    start_time = pygame.time.get_ticks()

def get_elapsed_time():
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    return elapsed_time

