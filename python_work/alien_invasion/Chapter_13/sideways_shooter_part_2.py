import sys
import pygame
from sideways_shooter_part_2_settings import SidewaysShooterPart2Settings
from sideways_shooter_part2_ship import Ship
from sideways_shooter_part_2_bullet import Bullet
from sideways_shooter_part_2_alien import Alien

DISTANCE_BETWEEN_ALIENS = 32

"""Sideway shooter where your ship in the left side of the screen, and aliens
attack from the right side. You can move up and down, shoot boolets in aliens, 
and when boolet have collision with alien, alien dissapear."""

class SidewaysShooterPart2:
    """Main class for the game"""
    
    def __init__(self):
        """Game and resourse initialization"""
        pygame.init()
        
        # An istance of settings class
        self.settings = SidewaysShooterPart2Settings()
        
        # Screen resolution and caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        
        pygame.display.set_caption("Sideway Shooter part 2")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Set the frame rate (e.g., 30 frames per second)
        self.clock = pygame.time.Clock()
        self.target_fps = 120
        
    def run_game(self):
        """Main loop where game runs"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            
        # Cap the frame rate to the target FPS
            self.clock.tick(self.target_fps)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)                    
                    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
            
    def fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet position
        self.bullets.update()
        
        # Get rid of bullets that have dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions()
                
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
        
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions of all
        aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
                
    def _create_fleet(self):
        """Create a fleet of aliens."""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // alien_height
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_width = self.ship.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width) - ship_width
        number_rows = available_space_x // (2 * alien_width)
    
        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = (alien_height + DISTANCE_BETWEEN_ALIENS * 2) * alien_number
        alien.rect.y = alien.y
        
        # Place aliens from the right side of the screen
        alien.rect.x = self.settings.screen_width - alien_width - alien_width * row_number
        
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Move left the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_move_left_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip ti the new screen."""
        # Redrawn the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)  
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
              
        # Make display visible        
        pygame.display.flip()
            
if __name__ == '__main__':
    # Making a game instance, and run the game
    sideway_shooter = SidewaysShooterPart2()
    sideway_shooter.run_game()