class SidewaysShooterPart2Settings:
    """A class to store sidewayshooter settings"""
    
    def __init__(self):
        """Game settings initialization"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 720
        
        # Background color
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_move_left_speed = 10
        # fleet_direction of -1 represents down; 1 represents up
        self.fleet_direction = -1
        