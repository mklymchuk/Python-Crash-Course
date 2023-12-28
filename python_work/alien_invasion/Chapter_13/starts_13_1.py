import pygame

class GridOfStars:
    """Class to make greed of stars on the screen"""
    
    def __init__(self):
        """Initialization of screen"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1280, 720))
        