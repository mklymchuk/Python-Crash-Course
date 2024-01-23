import pygame

SHIP_IMAGE = 'python_work/alien_invasion/images/sidewaysshotership.bmp'

class Ship:
    """A class to manage the ship"""

    def __init__(self, ss_game):
        """Ship and start position initialization"""
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.settings = ss_game.settings
        
        # Load image of the ship
        self.ship = pygame.image.load(SHIP_IMAGE)
        self.rect = self.ship.get_rect()
        
        # Start each new ship at the bottom in the left corner
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a decimal value for the ship's horizontal position
        self.y = float(self.rect.y)
        
        # Movement flags
        self.moving_down = False
        self.moving_up = False
    
    def update(self):
        """Update the ship's position based on the movement flags"""
        # Update the ship's value, not the rect
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            
        # Update rect object from self.y
        self.rect.y = self.y # type: ignore
                
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.ship, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)