# import pygame
import pygame
from sys import exit

# init pygame
pygame.init()

# create display surface
screen = pygame.display.set_mode((600, 400))  # this is set on x,y-axis. x = 800 y = 400. x, y read FROM left FROM top
# update game title
pygame.display.set_caption("Goblin Runner")
# create clock object to help control frame rate
clock = pygame.time.Clock()
hills_surface = pygame.image.load('images/hills.JPG')
ground_surface = pygame.image.load('images/ground.JPG')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # fill screen with color to wipe anything away from last frame
    screen.fill("purple")
    screen.blit(hills_surface, (0,0))
    screen.blit(ground_surface, ((0,320)))

    # update everything to keep display open
    pygame.display.update()
    # set frame rate ceiling
    clock.tick(60)
