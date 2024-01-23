class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # High score should never be reset
        self.high_score = self._read_high_score()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
        # Start Alien Invasion in an active state
        self.game_active = False
        
    def _read_high_score(self):
        """Read high score from file"""
        with open('python_work/alien_invasion/highscores.txt') as file:
            return int(file.read())