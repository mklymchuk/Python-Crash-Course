class SidewaysShooterPart2Settings:
    """A class to store sidewayshooter settings"""
    
    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 720
        
        # Background color
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_move_left_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        # How quickly alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
        # Easy settings speed modifyer
        self.easy_difficulty_speed_modifyer = 0.5
        
        # Hard settings speed modifyer
        self.hard_difficulty_speed_modifyer = 2
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction of -1 represents down; 1 represents up
        self.fleet_direction = -1
        
        # Scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings and alien points values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        
    def easy_difficulty(self):
        """Difficulty with 0.5 speed"""
        self.ship_speed = 1.5 * self.easy_difficulty_speed_modifyer
        self.bullet_speed = 3.0 * self.easy_difficulty_speed_modifyer
        self.alien_speed = 1.0 * self.easy_difficulty_speed_modifyer
        
        # fleet_direction of 1 represent right; -1 represent left
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
        
    def hard_difficulty(self):
        """Difficulty with 2x speed"""
        self.ship_speed = 1.5 * self.hard_difficulty_speed_modifyer
        self.bullet_speed = 3.0 * self.hard_difficulty_speed_modifyer
        self.alien_speed = 1.0 * self.hard_difficulty_speed_modifyer
        
        # fleet_direction of 1 represent right; -1 represent left
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
        