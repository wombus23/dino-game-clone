import sys
import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
done = False
GAME_CLOCK = pygame.time.Clock()
BACKGROUND_COLOR = (255, 255, 255)
GAME_WINDOW = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
ground_sprite = pygame.image.load("ground.png").convert_alpha()
dino_sprite = pygame.image.load("dino.png").convert_alpha()


pygame.display.set_caption("DINO CHROME RUNNER")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            exit()
        GAME_WINDOW.fill(BACKGROUND_COLOR)
        GAME_WINDOW.blit(ground_sprite, (-10, 150))
        pygame.display.flip()
        GAME_WINDOW.blit(dino_sprite, (10, 180))
        pygame.display.update()
        GAME_CLOCK.tick(60)
        print(GAME_CLOCK)










