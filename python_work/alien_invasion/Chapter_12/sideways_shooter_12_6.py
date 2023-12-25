import sys

import pygame

class SidewaysShooter:
    """A sideway shooter where ship starts on left side of the screen and allows
    the player to move the ship up and down. Ship fires a bullets that travels
    acros the screen when player presses the spacebar."""
    
    def __init__(self):
        """Initialization of game resourses"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1024, 600))
        pygame.display.set_caption("Sideways shooter")
        
        # Load ship and get it rect
        self.image = pygame.image.load('python_work/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start ship from left side
        self.rect.bottomleft = self.screen.get_rect().bottomleft
        # Set the beckground color
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Loop where game runs"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.bg_color)
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()

if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()