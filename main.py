import pygame
import math

pygame.init()

fps_clock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 200

gameState = False
ground_sprite = pygame.image.load("assets/ground.png")
player_character = pygame.image.load("assets/dino.png")
ground_width = ground_sprite.get_width()
ground_sprite = pygame.transform.scale(ground_sprite, (ground_width, WINDOW_HEIGHT))
cactus_sprite = pygame.image.load("assets/cactus.png")
player_character_rect = player_character.get_rect(midbottom=(100, 183))
cactus_rect = cactus_sprite.get_rect(bottomleft=(800, 180))
scroll = 0
tiles = math.ceil(WINDOW_WIDTH / ground_width) + 2
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("dino-game-clone")


while not gameState:
    fps_clock.tick(20)

    for i in range(tiles):
        screen.blit(ground_sprite, (i * ground_width + scroll - ground_width, 0))
    scroll -= 10
    if abs(scroll) > ground_width:
        scroll = 0

    screen.blit(player_character, player_character_rect)
    screen.blit(cactus_sprite, cactus_rect)

    cactus_rect.x -= 7
    if player_character_rect.colliderect(cactus_rect):
        print("Collision Detected")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = True
    pygame.display.flip()
pygame.quit()

