import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """Target for target practice"""
    
    def __init__(self, tp_game):
        """Target initialization"""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()
        
        # Build the rectangle target and place it on the right side of the screen
        self.rect = pygame.Rect(
            0, 0, self.settings.rectangle_width, self.settings.rectangle_height
        )
        self.rect.midright = (
            self.screen_rect.midright[0] - self.settings.screen_margin,
            self.screen_rect.midright[1]
        )
        
        # Store target exact position 
        self.y = float(self.rect.y)
        
    def draw_target(self):
        """Draw target"""
        self.screen.fill(self.settings.rect_color, self.rect)
        
    def move_target(self):
        """Move target up and down"""
        # Update target position based on the direction and speed 
        self.y += self.settings.target_direction * self.settings.target_speed
        
        # Update the rect based on value
        self.rect.y = int(self.y)

        # Check if the target reached bottom or top of the screen
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            
            # Reverse the direction of movement 
            self.settings.target_direction *= -1
