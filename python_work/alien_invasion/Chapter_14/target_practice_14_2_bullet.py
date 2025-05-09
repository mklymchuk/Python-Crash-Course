import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A bullet to shoot into the target"""
    
    def __init__(self, tp_game):
        """Creating bullet and resource initialization"""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen_rect
        
        # Build the bullet and place it on the screen
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midleft = (
            self.screen_rect.midleft[0] + self.settings.screen_margin, 
            self.screen_rect.midleft[1]
        )
        self.rect.midright = tp_game.ship.ship_rect.midright
        
        # Store bullet exact position
        self.x = float(self.rect.x)
        
    def update(self):
        """Move bullet on the screen"""
        self.x += self.settings.bullet_speed
        
        # Update rect position
        self.rect.x = self.x
        
    def draw_bullet(self):
        """Draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
