import pygame
import math

pygame.init()

fps_clock = pygame.time.Clock()

WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 210

gameState = True
ground_sprite = pygame.image.load("assets/ground.png")
player_character = pygame.image.load("assets/dino.png")
ground_width = ground_sprite.get_width()
ground_sprite = pygame.transform.scale(ground_sprite, (ground_width, WINDOW_HEIGHT))
cactus_sprite = pygame.image.load("assets/cactus.png")
player_character_rect = player_character.get_rect(midbottom=(100, 183))
cactus_rect = cactus_sprite.get_rect(bottomleft=(800, 189))
scroll = 0
tiles = math.ceil(WINDOW_WIDTH / ground_width) + 2
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("dino-game-clone")
player_gravity = 0

while True:
    fps_clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_character_rect.y >= 75:
                player_gravity = -28
    if gameState:
        for i in range(tiles):
            screen.blit(ground_sprite, (i * ground_width + scroll - ground_width, 0))
        scroll -= 10
        if abs(scroll) > ground_width:
            scroll = 0

        screen.blit(player_character, player_character_rect)
        screen.blit(cactus_sprite, cactus_rect)

        cactus_rect.x -= 7
        player_gravity += 2
        player_character_rect.y += player_gravity
        if player_character_rect.y >= 87:
            player_character_rect.y = 87
        if player_character_rect.colliderect(cactus_rect):
            gameState = False
    else:
        screen.fill('Red')

    pygame.display.update()

