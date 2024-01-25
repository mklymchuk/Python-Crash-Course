class GameStats:
    """Track statistick for Sideways shooter"""
    
    def __init__(self, ss_game):
        """Initialize statistics"""
        self.settings = ss_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state
        self.game_active = False
        
        # High score should never be reset
        self.high_score = self._read_high_score()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit   
        self.score = 0
        self.level = 1
        
    def _read_high_score(self):
        """Read high score from file"""
        with open('python_work/alien_invasion/Chapter_13/ss_game_highscores.txt') as file:
            return int(file.read())