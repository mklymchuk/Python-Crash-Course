import sys
import pygame
from random import randint

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class GridOfStars:
    """Class to make grid of stars on the screen"""
    
    def __init__(self):
        """Initialization of screen"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        
        pygame.display.set_caption("Grid of stars")
        
        self.image = pygame.image.load('python_work/alien_invasion/images/gold_star.bmp')
        self.star_width, self.star_height = self.image.get_rect().size
        
        self.bg_color = (255, 255, 255)
        
    def run_game(self):
        """Loop where game runs"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self._grid_of_stars()
            pygame.display.flip()
            
            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(5) / 1000
            
    def _grid_of_stars(self):
        """Make grid of stars"""
        # Background color
        self.screen.fill(self.bg_color)
        
        for i in range(0, 10):
            random_number = randint(-10, 10)
            star_x = random_number * self.star_width
            random_number = randint(-10, 10)
            star_y = random_number * self.star_height
            star_rect = pygame.Rect(star_x, star_y, self.star_width, self.star_height)
            self.screen.blit(self.image, star_rect.topleft)
        
if __name__ == '__main__':
    grid_of_stars = GridOfStars()
    grid_of_stars.run_game()
