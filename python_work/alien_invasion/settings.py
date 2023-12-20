class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        blue_sky_color = (127, 207, 240)
        
        # Screen setttings
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (230, 230, 230)
        self.bg_color = blue_sky_color
        
        # Ship settings
        self.ship_speed = 1.5