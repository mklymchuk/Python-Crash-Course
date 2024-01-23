import sys
import pygame
from pygame.sprite import Group, Sprite

SHIP_SPEED = 1

class Bullet(Sprite):
    """A class to represent bullets."""
    
    def __init__(self, sidewa_shooter):
        super().__init__()
        self.screen = sidewa_shooter.screen
        self.settings = sidewa_shooter.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = sidewa_shooter.rect.midtop
        
        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the bullet from left to right."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

class SidewaysShooter:
    """A sideway shooter where the ship starts on the left side of the screen and allows
    the player to move the ship up and down. The ship fires bullets that travel
    across the screen when the player presses the spacebar."""
    
    def __init__(self):
        """Initialization of game resources"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1024, 600))
        pygame.display.set_caption("Sideways shooter")
        
        # Load the ship and get its rect
        self.image = pygame.image.load('python_work/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.angle = -90
        self.rotate_image = pygame.transform.rotate(self.image, self.angle)
        # Start the ship from the left side
        self.rect.bottomleft = self.screen.get_rect().bottomleft
        # Set the background color
        self.bg_color = (230, 230, 230)
        
        # Bullet settings
        self.settings = BulletSettings()
        
        # Create a Group to store bullets
        self.bullets = Group()
        
    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
    def run_game(self):
        """Loop where the game runs"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fire_bullet()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= SHIP_SPEED
            if keys[pygame.K_DOWN] and self.rect.y < self.screen.get_rect().height - self.rect.height:
                self.rect.y += SHIP_SPEED
            
            self.screen.fill(self.bg_color)
            
            # Update and draw bullets
            self.bullets.update()
            for bullet in self.bullets:
                pygame.draw.rect(self.screen, self.settings.bullet_color, bullet.rect)

            self.screen.blit(self.rotate_image, self.rect)
            pygame.display.flip()

class BulletSettings:
    """A class to store bullet settings."""
    
    def __init__(self):
        """Initialize bullet settings."""
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()
