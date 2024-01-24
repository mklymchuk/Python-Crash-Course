class GameStats:
    """Track statistick for Sideways shooter"""
    
    def __init__(self, ss_game):
        """Initialize statistics"""
        self.settings = ss_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state
        self.game_active = False
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit   
        self.score = 0