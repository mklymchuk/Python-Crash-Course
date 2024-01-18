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
        self.bullet_width, self.bullet_height = 15, 3
        self.bullet_speed = 3
        self.bullet_color = (255, 0, 0)
        
        # Play Button settings
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)       
        
        # Players life
        self.players_life = 3 
        