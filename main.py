# import pygame
import pygame
from sys import exit
# init pygame
pygame.init()

# create display surface
screen = pygame.display.set_mode((800, 400))
# update game title
pygame.display.set_caption("Goblin Runner")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all elements
    # update everything to keep display open
    pygame.display.update()
