import pygame
from timer import*
pygame.init()




def button(msg,x,y,w,h,ic,ac,action=None):
    global screen,black,bright_green,bright_red
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
          pygame.draw.rect(screen,ac,(x,y,w,h))
          if click[0]==1 and action!=None:
               action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    t=pygame.font.SysFont('ComicSans.ttf',20)
    ts,tr=text_objects(msg,t)
    tr.center=(x+w/2,y+h/2)
    screen.blit(ts,tr)

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()


