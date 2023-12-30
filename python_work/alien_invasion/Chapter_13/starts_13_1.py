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
        self.star_width, self.star_height = self.image.get_rect().size
        self.bg_color = (255, 255, 255)
        
    def run_game(self):
        """Loor where game runs"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self._grid_of_stars()
            self.screen.fill(self.bg_color)
            
            pygame.display.flip()
            
    def _grid_of_stars(self):
        """Make grid of stars"""
        number_of_stars_in_row = SCREEN_WIDTH // self.star_width
        number_of_rows = SCREEN_HEIGHT // self.star_height
        
        for row_number in range(number_of_rows):
            for star_number in range(number_of_stars_in_row):
                star_x = star_number * self.star_width
                star_y = row_number * self.star_height
                star_rect = pygame.Rect(star_x, star_y, self.star_width, self.star_height)
                self.screen.blit(self.image, star_rect.topleft)
        
if __name__ == '__main__':
    grid_of_stars = GridOfStars()
    grid_of_stars.run_game()