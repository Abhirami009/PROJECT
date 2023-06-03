import pygame
import sys
from helper import text_objects
from timer import*











def carselection():
    global screen,clock
    car1 = pygame.image.load('car1.png')
    car2 = pygame.image.load('car2.png')
    car3 = pygame.image.load('car3.png')

    screen.fill((255, 255, 255))  # Fill the screen with white color
    text = pygame.font.SysFont('ComicSans', 40)
    text_surface, text_rect = text_objects('Select Your Car', text)
    text_rect.center = (400, 50)
    screen.blit(text_surface, text_rect)

    # Display car options
    screen.blit(car1, (100, 150))
    screen.blit(car2, (300, 150))
    screen.blit(car3, (500, 150))

    selected_car = None

    while not selected_car:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 100 <= mouse_pos[0] <= 200 and 150 <= mouse_pos[1] <= 250:
                    selected_car = 'car1.png'
                elif 300 <= mouse_pos[0] <= 400 and 150 <= mouse_pos[1] <= 250:
                    selected_car = 'car2.png'
                elif 500 <= mouse_pos[0] <= 600 and 150 <= mouse_pos[1] <= 250:
                    selected_car = 'car3.png'

        pygame.display.update()
        clock.tick(20)

    return selected_car