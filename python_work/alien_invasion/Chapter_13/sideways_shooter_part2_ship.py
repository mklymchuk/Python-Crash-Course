import pygame

SHIP_IMAGE = 'python_work/alien_invasion/images/sidewaysshotership.bmp'

class Ship:
    """A class to manage the ship"""

    def __init__(self, ss_game):
        """Ship and start position initialization"""
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        
        # Load image of the ship
        self.ship = pygame.image.load(SHIP_IMAGE)
        self.rect = self.ship.get_rect()
        
        # Start each new ship at the bottom in the left corner
        self.rect.bottomleft = self.screen_rect.bottomleft
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.ship, self.rect)