import sys
import pygame
from pygame.sprite import Group, Sprite

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

RAINDROP = 'python_work/alien_invasion/images/raindrop.bmp'

class Raindrop(Sprite):
    """A class to represent a raindrop."""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(RAINDROP)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        """Move the raindrop down."""
        self.rect.y += 1

class Raindrops:
    """Raindrops on the screen"""
    
    def __init__(self):
        """Raindrops initialization on the screen"""
        pygame.init()
        
        # Display settings
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        
        # Distance between raindrops taken from image width, and height
        self.raindrop_image = pygame.image.load(RAINDROP)
        self.raindrop_width, self.raindrop_height = self.raindrop_image.get_rect().size
        
        pygame.display.set_caption("Raindrops")
        
        # Resource load
        self.raindrops_group = Group()
        
        # Screen background color
        self.bg_color = (255, 255, 255)
        
        self._create_raindrops()
        
    def run_rain(self):
        """Run rain"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self._rain()
            pygame.display.flip()
    
    def _rain(self):
        """Where rain created"""
        self.screen.fill(self.bg_color)
        self.raindrops_group.update()
        self.raindrops_group.draw(self.screen)
                
    def _create_raindrops(self):
        """Create a grid of raindrops."""
        number_of_raindrops_in_row = DISPLAY_WIDTH // self.raindrop_width
        number_of_rows = DISPLAY_HEIGHT // self.raindrop_height
        
        for row in range(number_of_rows):
            for raindrop_number in range(number_of_raindrops_in_row):
                raindrop_x = raindrop_number * self.raindrop_width
                raindrop_y = row * self.raindrop_height
                raindrop = Raindrop(raindrop_x, raindrop_y)
                self.raindrops_group.add(raindrop)
    
    def _check_rain_edge(self):
        """Return True if raindrop is on the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.down >= screen_rect.down:
            return True
            
if __name__ == '__main__':
    raindrops = Raindrops()
    raindrops.run_rain()
