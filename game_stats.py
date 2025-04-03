class GameStats():
    """Kontrollib mängu statistikat"""
    
    
    def __init__(self):
        """Initsialiseeri statistika"""
        self.game_active = False
        self.reset_stats()
        
        
    def reset_stats(self):
        """Initsialiseeri skoor, mis saab muutuda mängu ajal"""
        self.score = 0
        self.level = 1
        self.bonus = 0