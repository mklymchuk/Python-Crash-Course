import sys

import pygame

from character import Character

class DrawCharacter:
    """Draw bitmap character in center of the screen"""
    
    def __init__(self):
        """Initialize resourses"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((320, 240))
        pygame.display.set_caption("Character in centre")
        
        self.character = Character(self)
        
        self.bg_color = (127, 207, 240)
        
        
    def run_game(self):
        """Run screen refresh"""
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.bg_color)
            self.character.blitme()
            
            pygame.display.flip()
        
if __name__ == '__main__':
    # Make a instance and run
    dc = DrawCharacter()
    dc.run_game()
    