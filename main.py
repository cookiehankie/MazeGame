import pygame
import config
from player import Player


pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player()

running = True
# realize [config.FPS] Frames Per Second (FPS)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    player.update()
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    # everytime arrives this line the app will stop for 1/60 second
    clock.tick(config.FPS)

pygame.quit()
