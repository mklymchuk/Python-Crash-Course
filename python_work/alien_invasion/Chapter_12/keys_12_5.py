import sys

import pygame

class EmptyScreen:
    """Create empty screen with event loop"""
    
    def __init__(self):
        """Resourse initialization"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Empty screen with event")
        
        
    def run_game(self):
        """Loop what run a game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    
            pygame.display.flip()
            
if __name__ == '__main__':
    empty_screen = EmptyScreen()
    empty_screen.run_game()