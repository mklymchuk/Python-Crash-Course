import pygame

class Ship:
    """A ship for target practice game"""
    
    def __init__(self, tp_game):
        """A ship initialization"""
        
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect
        
        # Load ship image
        self.ship_image = 'python_work/alien_invasion/images/triangle_ship.bmp'
        self.ship = pygame.image.load(self.ship_image)
        
        # Get ship rect
        self.ship_rect = self.ship.get_rect()
        
        # Start each new ship from left side mid position of the screen
        self.ship_rect.midleft = self.screen_rect.midleft
        
        # Movement flag
        self.moving_up = False
        
    def update(self):
        """Update ship position based on movement flag"""
        if self.moving_up:
            self.ship_rect.y -= 1
            
    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.ship, self.ship_rect)