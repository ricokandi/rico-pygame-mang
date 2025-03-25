import sys
import pygame
from player import Player

def check_events(player):
    """Kontrolli klaviatuuri vajutusi"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
            
            
def update_screen(game_settings, screen, player):
    """Uuenda ekraani pilti ja joonista uus ekraan"""
    screen.fill(game_settings.bg_colour)
    player.blit_me()
    pygame.display.flip()