import sys
import pygame
from sideways_shooter_part_2_settings import SidewaysShooterPart2Settings
from sideways_shooter_part2_ship import Ship

"""Sideway shooter where your ship in the left side of the screen, and aliens
attack from the right side. You can move up and down, shoot boolets in aliens, 
and when boolet have collision with alien, alien dissapear."""

class SidewaysShooterPart2:
    """Main class for the game"""
    
    def __init__(self):
        """Game and resourse initialization"""
        pygame.init()
        
        # An istance of settings class
        self.settings = SidewaysShooterPart2Settings()
        
        # Screen resolution and caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        
        pygame.display.set_caption("Sideway Shooter part 2")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """Main loop where game runs"""
        while True:
            self._check_events()
            self.ship.update()
            self._fill_the_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        # Move the ship down
                        self.ship.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = False
                    
    def _fill_the_screen(self):
        """Update images on the screen, and flip ti the new screen."""
        # Redrawn the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)  
        self.ship.blitme()
              
        # Make display visible        
        pygame.display.flip()
            
if __name__ == '__main__':
    # Making a game instance, and run the game
    sideway_shooter = SidewaysShooterPart2()
    sideway_shooter.run_game()
                    
                    