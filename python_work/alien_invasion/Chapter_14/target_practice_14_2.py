import sys

import pygame

SHIP_IMAGE = 'python_work/alien_invasion/images/triangle_ship.bmp'
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class TargetPractice:
    """A target practice game, where a player shoots a rectangle, and if he 
    misses three times - game ends"""
    
    def __init__(self):
        """Game initialization, and resourse load"""
        
        pygame.init()
        
        self.ship = pygame.image.load(SHIP_IMAGE)
        self.ship_rect = self.ship.get_rect()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Target practice")
        
        self.ship_rect.midleft = self.screen_rect.midleft
        
        self.bg_color = (224, 255, 255)
        
        # Movement flag
        self.moving_up = False
        
    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
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
            self._update()
        elif event.key == pygame.K_DOWN:
            self.ship_rect.y += 1
            
    def _update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_up:
            self.ship_rect.y -= 1
                            
    def _update_screen(self):
        """Update screen"""
        self.screen.fill(self.bg_color)
        self.screen.blit(self.ship, self.ship_rect)
            
if __name__ == '__main__':
    """Making an instance of Target Practice"""
    target_practice = TargetPractice()
    target_practice.run_game()