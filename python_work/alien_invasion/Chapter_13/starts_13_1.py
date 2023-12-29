import sys

import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class GridOfStars:
    """Class to make greed of stars on the screen"""
    
    def __init__(self):
        """Initialization of screen"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        pygame.display.set_caption("Greed of stars")
        
        self.image = pygame.image.load('python_work/alien_invasion/images/gold_star.bmp')
        self.rect = self.image.get_rect()
        
        self.bg_color = (255, 255, 255)
        
    def run_game(self):
        """Loor where game runs"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self._grid_of_stars()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.image, self.rect)
            
            pygame.display.flip()
            
    def _grid_of_stars(self):
        """Make grid of stars"""
        
if __name__ == '__main__':
    grid_of_stars = GridOfStars()
    grid_of_stars.run_game()