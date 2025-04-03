import pygame.font


class Button():
    """Klass nupu objekti jaoks"""
    
    
    def __init__(self, game_settings, screen, msg):
        """Init nupu atribuudid"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #nupu atribuudid - suurus, värv, font
        self.width = 200
        self.height = 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        #Ehitame nupu
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #graafikaline tekst
        self.prepare_msg(msg)
        
        
    def prepare_msg(self, msg):
        """Teisenda nupu kiri füüsiliseks ja nupu keskele"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)