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
# init font
goblin_font = pygame.font.Font('fonts/zeropixel-eye-fs.ttf', 50)

# init surfaces
hills_surface = pygame.image.load('images/hills.JPG')
ground_surface = pygame.image.load('images/ground.JPG')
text_surface = goblin_font.render('Goblin Runner', False, 'black')
snail_surface = pygame.image.load('images/enemy/snail1.png')

# init surface positions
snail_x_pos = 600
snail_y_pos = 320

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # fill screen with color to wipe anything away from last frame
    screen.fill("purple")
    screen.blit(hills_surface, (0, 0))
    screen.blit(ground_surface, (0, 320))
    screen.blit(text_surface, (70, 25))
    snail_x_pos -= 3
    if snail_x_pos < -100:
        snail_x_pos = 600

    screen.blit(snail_surface,(snail_x_pos, snail_y_pos))

    # update everything to keep display open
    pygame.display.update()
    # set frame rate ceiling
    clock.tick(60)
