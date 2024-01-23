class GameStats:
    """Track statistick for Alien Invasion"""
    
    def __init__(self, tp_game):
        """Initialize statistics"""
        self.settings = tp_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize statistick that can change during the game"""
        # Start Alien Invasion in an active state
        self.game_active = False