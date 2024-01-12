class Settings:
    """A class to store target practice settings"""
    
    def __init__(self):
        """Game settings initialization"""
        
        # Screen resolution
        self.screen_width = 1280
        self.screen_height = 720
        
        # Background color
        self.bg_color = (224, 255, 255)
        
        # Margin for target and ship
        self.screen_margin = 20
        
        # Ship speed
        self.ship_speed = 1.5
        
        # Target size
        self.rectangle_width, self.rectangle_height = 64, 64
        
        # Target color
        self.rect_color = (0, 0, 0)
        
        # Target speed
        self.target_speed = 0.1
        
        