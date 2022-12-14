import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
base_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_surf = base_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 30))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (750, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50, 300))
player_gravity = 0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10, 6)
        screen.blit(score_surf, score_rect)
        screen.blit(snail_surface, snail_rect)
        
        if snail_rect.right <= 0:
            snail_rect.left = 800
        snail_rect.left -= 4

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Red')

    pygame.display.update()
    clock.tick(60)
    