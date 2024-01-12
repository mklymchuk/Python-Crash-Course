import pygame

class Ship:
    """A ship for target practice game"""
    
    def __init__(self, tp_game):
        """Ship initialization"""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()
        
        # Load ship image
        self.ship_image = 'python_work/alien_invasion/images/triangle_ship.bmp'
        self.ship = pygame.image.load(self.ship_image)
        
        # Get ship rect
        self.ship_rect = self.ship.get_rect()
        
        # Start each new ship from the left side mid position of the screen
        self.ship_rect.midleft = self.screen_rect.midleft
        
        # Store a decimal value for the ship's vertical position
        self.y = float(self.ship_rect.y)
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update ship's position based on the movement flags"""
        # Update the ship y value, not the rect
        if self.moving_up and self.ship_rect.top < 0:
            self.ship_rect.y -= self.settings.ship_speed
        if self.moving_down and self.ship_rect.bottom > self.screen_rect.bottom:
            self.ship_rect.y += self.settings.ship_speed
            
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.ship, self.ship_rect)
