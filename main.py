# import pygame
import pygame
from random import randint
from sys import exit


# CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200, 300))


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 345:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = goblin_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(300, 45))
    screen.blit(score_surf, score_rect)
    return current_time


def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 345:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]
    # player walking animation if player is on the floor
    # display jump surface when player is not on floor


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
goblin_font = pygame.font.Font('fonts/zeropixel-eye-fs.ttf', 40)

game_active = False
start_time = 0
game_over_surf = goblin_font.render('Snail Runner', False, (210, 4, 45))
game_over_rect = game_over_surf.get_rect(center=(300, 25))
game_instructions = goblin_font.render("Press 'space' to run", False, (210, 4, 45))
game_instructions_rect = game_instructions.get_rect(center=(295, 85))
score = display_score()

player = Player()

# init surfs and rects
hills_surf = pygame.image.load('images/hills.JPG').convert_alpha()
ground_surf = pygame.image.load('images/ground.JPG').convert_alpha()

# score_surf = goblin_font.render('Snail Runner', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(300, 45))

player_walk_1 = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('images/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_jump = pygame.image.load('images/player/jump.png').convert_alpha()
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(70, 345))
player_gravity = 0

player_stand = pygame.image.load('images/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(285, 300))

# OBSTACLES

# snail
snail_frame_1 = pygame.image.load('images/enemy/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('images/enemy/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surf = snail_frames[snail_index]

# fly
fly_frame_1 = pygame.image.load('images/fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('images/fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surf = fly_frames[fly_index]

obstacle_rect_list = []

# TIMERS
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
            if event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(800, 1000), 345)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(800, 1000), 220)))
            if event.type == snail_animation_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail_surf = snail_frames[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly_surf = fly_frames[fly_index]

    if game_active:
        screen.fill("purple")
        screen.blit(hills_surf, (0, 0))
        screen.blit(ground_surf, (0, 320))
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.right = 800

        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 345:
            player_rect.bottom = 345
        player_animation()
        screen.blit(player_surf, player_rect)

        # OBSTACLE MOVEMENT
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # COLLISIONS
        game_active = collision(player_rect, obstacle_rect_list)

    else:  # Game over state
        screen.fill((94, 129, 162))
        obstacle_rect_list.clear()
        player_rect.bottom = 345
        player_gravity = 0

        screen.blit(game_over_surf, game_over_rect)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_instructions, game_instructions_rect)
        score_message = goblin_font.render(f'Your score: {score}', False, (210, 4, 45))
        score_message_rect = score_message.get_rect(center=(285, 150))

        if score == 0:
            screen.blit(game_instructions, game_instructions_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # update everything to keep display open
    pygame.display.update()
    # set frame rate ceiling
    clock.tick(60)
