import pygame
from settings import Settings


pygame.init()
gm_set = Settings()

screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("mediumblue")
    pygame.display.set_caption("Bubble Bluster")
    
    
    
    
    
    
    pygame.display.flip()
pygame.quit()