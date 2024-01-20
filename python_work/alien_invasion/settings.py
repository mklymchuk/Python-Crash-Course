class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        blue_sky_color = (127, 207, 240)
        
        # Screen setttings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = blue_sky_color
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction of 1 represent right; -1 represent left
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
    def easy_difficulty(self):
        """Difficulty with 0.5 speed"""
        self.ship_speed = 1.5 * 0.5
        self.bullet_speed = 3.0 * 0.5
        self.alien_speed = 1.0 * 0.5
        
    def hard_difficulty(self):
        """Difficulty with 2x speed"""
        self.ship_speed *= 2
        self.bullet_speed *= 2
        self.alien_speed *= 2