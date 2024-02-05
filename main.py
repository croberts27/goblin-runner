# import pygame
import pygame
from sys import exit

# init pygame
pygame.init()

# create display surf
dis_width = 600
dis_height = 400

# this is set on x,y-axis. x = 800 y = 400. x, y read FROM left FROM top
screen = pygame.display.set_mode((dis_width, dis_height))

# update game title
pygame.display.set_caption("Goblin Runner")

# create clock object to help control frame rate
clock = pygame.time.Clock()
# init font
goblin_font = pygame.font.Font('fonts/zeropixel-eye-fs.ttf', 50)

# init surfs
hills_surf = pygame.image.load('images/hills.JPG').convert_alpha()
ground_surf = pygame.image.load('images/ground.JPG').convert_alpha()
text_surf = goblin_font.render('Goblin Runner', False, 'black')
snail_surf = pygame.image.load('images/enemy/snail1.png').convert_alpha()
player_surf = pygame.image.load('images/player/player_walk_1.png').convert_alpha()

# rectangles
player_rect = player_surf.get_rect(midbottom=(70, 345))
snail_rect = snail_surf.get_rect(bottomright=(800, 345))

# init surf positions
snail_y_pos = 320

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # fill screen with color to wipe anything away from last frame
    screen.fill("purple")
    screen.blit(hills_surf, (0, 0))
    screen.blit(ground_surf, (0, 320))
    screen.blit(text_surf, (70, 25))
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    if player_rect.colliderect(snail_rect):
        exit()

    # update everything to keep display open
    pygame.display.update()
    # set frame rate ceiling
    clock.tick(60)
