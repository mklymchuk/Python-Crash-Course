class Settings:
    """A class to store target practice settings"""
    
    def __init__(self):
        """Game settings initialization"""
        
        # Screen resolution
        self.screen_width = 1280
        self.screen_height = 720
        
        # Background color
        self.bg_color = (225, 255, 255)
        
        # Margin for target and ship
        self.screen_margin = 20
        
        # Ship speed
        self.ship_speed = 1.5
        
        # Target settings
        self.rectangle_width, self.rectangle_height = 64, 64
        self.rect_color = (0, 0, 0)
        self.target_speed = 0.1
        self.target_direction = -1 # -1 top, 1 bottom
        
        # Bullet settings
        self.bullet_width, self.bullet_height = 3, 3
        self.bullet_speed = 3
        self.bullet_color = (233, 233, 233)
        
        