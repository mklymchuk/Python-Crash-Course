import pygame

ROCKET_SPEED = 1

class RocketShip:
    """A class to manage rocket"""
    
    def __init__(self, rocket_12_4):
        """Initialize a rocket and position"""
        self.screen = rocket_12_4.screen
        self.position = rocket_12_4.screen.get_rect()
        
        # Load rocket image, and get it rect
        self.image = pygame.image.load('python_work/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each rocket at centre of the screen 
        self.rect.center = self.screen.get_rect().center
        
        # Rocket movement
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update rocket position"""
        self.screen.blit(self.image, self.rect)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= ROCKET_SPEED
        if keys[pygame.K_DOWN] and self.rect.y < self.screen.get_rect().height - self.rect.height:
            self.rect.y += ROCKET_SPEED
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= ROCKET_SPEED
        if keys[pygame.K_RIGHT] and self.rect.x < self.screen.get_rect().width - self.rect.width:
            self.rect.x += ROCKET_SPEED