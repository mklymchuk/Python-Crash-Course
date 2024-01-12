import sys

import pygame

from target_practice_14_2_settings import Settings
from target_practice_14_2_ship import Ship

class TargetPractice:
    """A target practice game, where a player shoots a rectangle, and if he 
    misses three times - game ends"""
    
    def __init__(self):
        """Game initialization, and resourse load"""
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Target practice")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
            pygame.display.flip()
            
    def _check_events(self):
        """Key and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        """Check if any key pressed"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
                            
    def _update_screen(self):
        """Update screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
if __name__ == '__main__':
    """Making an instance of Target Practice"""
    target_practice = TargetPractice()
    target_practice.run_game()