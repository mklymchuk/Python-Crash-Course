import sys
import pygame

"""Sideway shooter where your ship in the left side of the screen, and aliens
attack from the right side. You can move up and down, shoot boolets in aliens, 
and when boolet have collision with alien, alien dissapear."""

class SidewayShooterPart2:
    """Main class for the game"""
    
    def __init__(self):
        """Game and resourse initialization"""
        pygame.init()
        
        # Screen resolution and caption
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Sideway Shooter part 2")
        
        # Background color
        self.bg_color = (230, 230, 230)
        
        # Load image of the ship
        self.ship = pygame.image.load('python_work/alien_invasion/images/ship.bmp')
        
    def run_game(self):
        """Main loop where game runs"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redrawn the screen during each pass through the loop
            self.screen.fill(self.bg_color)   
              
            # Make display visible        
            pygame.display.flip()
            
if __name__ == '__main__':
    # Making a game instance, and run the game
    sideway_shooter = SidewayShooterPart2()
    sideway_shooter.run_game()
                    
                    