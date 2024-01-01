import sys
import pygame

DISPLAY_WIDTH = 1280.0
DISPLAY_HEIGHT = 720.0

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
        
        # Screen background color
        self.bg_color = (255, 255, 255)
        
    def run_rain(self):
        """Run rain"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
if __name__ == '__main__':
    raindrops = Raindrops()
    raindrops.run_rain()