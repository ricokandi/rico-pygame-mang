import pygame
from settings import Settings
from button import Button
from player import Player
from bubble import Bubble
from scoreboard import Scoreboard
from game_stats import GameStats
import game_functions as gf


def run_game():
    pygame.init()
    gm_set = Settings()

    screen = pygame.display.set_mode([gm_set.screen_width, gm_set.screen_height])
    pygame.display.set_caption(gm_set.caption)
    
    #Initsialisserime "play" nupu
    play_button = Button(gm_set, screen, "Play")
    
    #Initsialiseerime mängu skoori
    stats = GameStats()
    
    #Initsialiseerime tulemustabel
    sb = Scoreboard(gm_set, screen, stats)
    
    #Loome kella, et mängu kaadrit sekundis oleks normaalne
    clock = pygame.time.Clock()
    
    #Initsialiseerib mängija
    player = Player(screen)
    
    #Loob grupid, et hoida mulle
    bubbles = pygame.sprite.Group()

    #Jookse kuni mängija nõuab, et mäng peatuks
    while True:
        gf.check_events(gm_set, screen, player, bubbles, stats, play_button)
        if stats.game_active:
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb)
            bubbles.update()
        else:
            bubbles.empty()
        gf.update_screen(gm_set, screen, player, bubbles, clock, stats, play_button, sb)
run_game()
