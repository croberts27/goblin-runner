# import pygame
import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = goblin_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(300, 45))
    screen.blit(score_surf, score_rect)


# init pygame
pygame.init()

# create display surf
# this is set on x,y-axis. x = 800 y = 400. x, y read FROM left FROM top
screen = pygame.display.set_mode((600, 400))

# update game title
pygame.display.set_caption("Snail Runner")

# create clock object to help control frame rate
clock = pygame.time.Clock()
# init font
goblin_font = pygame.font.Font('fonts/zeropixel-eye-fs.ttf', 50)

game_active = False
start_time = 0
game_over_surf = goblin_font.render('GAME OVER!', False, (210, 4, 45))
game_over_rect = game_over_surf.get_rect(center=(300, 50))
restart_surf = goblin_font.render("'R' TO RESTART", False, (210, 4, 45))
restart_rect = game_over_surf.get_rect(center=(240, 150))

# init surfs and rects
hills_surf = pygame.image.load('images/hills.JPG').convert_alpha()
ground_surf = pygame.image.load('images/ground.JPG').convert_alpha()

# score_surf = goblin_font.render('Snail Runner', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(300, 45))

player_surf = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(70, 345))
player_gravity = 0

player_stand = pygame.image.load('images/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(280, 300))

snail_surf = pygame.image.load('images/enemy/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(800, 345))

# CLASSES


# init surf positions
snail_y_pos = 320

# WHILE LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 345:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN and player_rect.bottom >= 345:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        if not game_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.fill("purple")
        screen.blit(hills_surf, (0, 0))
        screen.blit(ground_surf, (0, 320))
        screen.blit(snail_surf, snail_rect)
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.right = 800

        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 345:
            player_rect.bottom = 345
        screen.blit(player_surf, player_rect)

        # Collision detection
        if player_rect.colliderect(snail_rect):  # Check collision with snail_rect
            game_active = False

    else:  # Game over state
        screen.fill((94, 129, 162))
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(player_stand, player_stand_rect)

    # update everything to keep display open
    pygame.display.update()
    # set frame rate ceiling
    clock.tick(60)
