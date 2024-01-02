import sys
import pygame
from pygame.sprite import Group, Sprite

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

RAINDROP = 'python_work/alien_invasion/images/raindrop.bmp'

class Raindrops:
    """Raindrops on the screen"""
    
    def __init__(self):
        """Raindrops initialization on the screen"""
        pygame.init()
        
        # Display settings
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Raindrops")
        
        # Resourse load
        self.raindrop_image = pygame.image.load(RAINDROP)
        self.raindrop_width, self.raindrop_height = self.raindrop_image.get_rect().size
        
        # Screen background color
        self.bg_color = (255, 255, 255)
        
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
        
        number_of_raindrops_in_row = DISPLAY_WIDTH // self.raindrop_width
        number_of_rows = DISPLAY_HEIGHT // self.raindrop_height
        
        for raindrop in  range(number_of_rows):
            for raindrop_number in range(number_of_raindrops_in_row):
                raindrop_x = raindrop_number * self.raindrop_width
                raindrop_y = raindrop * self.raindrop_height
                raindrop_rect = pygame.Rect(raindrop_x, raindrop_y, self.raindrop_width, self.raindrop_height)
                self._raindrop(number_of_rows)
                self.screen.blit(self.raindrop_image, raindrop_rect.topleft)
                
    def _raindrop(self, number_of_rows):
        """Drop an entire grid of raindrops"""
        raindrop_speed = 1
        for raindrop in range(number_of_rows):
            raindrop.rect.y += raindrop_speed
            
                        
if __name__ == '__main__':
    raindrops = Raindrops()
    raindrops.run_rain()