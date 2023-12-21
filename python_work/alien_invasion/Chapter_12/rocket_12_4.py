import sys

import pygame
from rocket import RocketShip

class Rocket:
    """Game that begins with a rocket in the centre of the screen. Player can
    move rocket up, down, left, or right using the arrow keys"""
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rocket in cetre of the screen")
        self.bg_color = (204, 255, 255)
        
        self.rocket_ship = RocketShip(self)
        
    def run_game(self):
        """Loop what run game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.bg_color)
            
            self.rocket_ship.update()
                
            pygame.display.flip()
                    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    rocket = Rocket()
    rocket.run_game()