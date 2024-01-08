import pygame
from pygame.sprite import Sprite

DISTANCE_BETWEEN_ALIENS = 32

class Alien(Sprite):
    """A class to represent alien in the fleet"""
    
    def __init__(self, ss_game):
        """Initialize the alien and set its rect attribute"""
        super().__init__()
        self.screen = ss_game.screen
        
        # Load the alien image and set ist rect attribute
        self.image = pygame.image.load('python_work/alien_invasion/images/alien_spider.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the right top of the screen
        self.rect.x = ss_game.settings.screen_width - self.rect.width
        self.rect.y = DISTANCE_BETWEEN_ALIENS
        
        # Store the alien's exact vertical position
        self.y = float(self.rect.y)