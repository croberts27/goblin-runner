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

score_surf = goblin_font.render('Score: ', False, 'black')
score_rect = score_surf.get_rect(center=(125, 25))

player_surf = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(70, 345))

snail_surf = pygame.image.load('images/enemy/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(800, 345))


# classes

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.health = 100
        # isJump and jumpCount should be attributes of Player.
        self.isJumping = False
        self.isFalling = False


# init surf positions
snail_y_pos = 320

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
    # fill screen with color to wipe anything away from last frame
    screen.fill("purple")
    screen.blit(hills_surf, (0, 0))
    screen.blit(ground_surf, (0, 320))
    screen.blit(score_surf, score_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(snail_surf, snail_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.right = 800

    # if player_rect.colliderect(snail_rect):
    #     exit()

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    # update everything to keep display open
    pygame.display.update()
    # set frame rate ceiling
    clock.tick(60)
