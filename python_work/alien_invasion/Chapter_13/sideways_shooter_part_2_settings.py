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
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3