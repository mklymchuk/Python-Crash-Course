import pygame

class Character:
    """A class to manage character"""
    
    def __init__(self, dc):
        """Initialize character and starting position"""
        self.screen = dc.screen
        self.screen_rect = dc.screen.get_rect()
        
        self.image = pygame.image.load('python_work/alien_invasion/images/cube_face.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
               
    def blitme(self):
        """Initialize the character"""
        self.screen.blit(self.image, self.rect)