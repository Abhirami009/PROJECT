import pygame
import sys
from gameloop import intro

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        intro()

if __name__ == "__main__":
    main()