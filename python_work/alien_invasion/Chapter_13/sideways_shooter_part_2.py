import sys
from time import sleep

import pygame

from sideways_shooter_part_2_settings import SidewaysShooterPart2Settings
from sideways_shooter_part_2_game_stats import GameStats
from sideways_shooter_part_2_scoreboard import Scoreboard
from sideways_shooter_part_2_button import Button
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
        
        # Create an instance to store game statistics, and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Set the frame rate (e.g., 30 frames per second)
        self.clock = pygame.time.Clock()
        self.target_fps = 120
        
        self.buttons_initialization()
        
    def run_game(self):
        """Main loop where game runs"""
        while True:
            self._check_events()
            
            if self.stats.game_active:  
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            
        # Cap the frame rate to the target FPS
            self.clock.tick(self.target_fps)
            
    def buttons_initialization(self):
        """Button initialization"""
        # Make the play button
        screen_center_x = self.settings.screen_width // 2
        screen_center_y = self.settings.screen_height // 2
        self.play_button = Button(
            self, "Play", screen_center_x - 100, screen_center_y - 150
            )
        # Make difficulty buttons
        self.easy_difficulty_button = Button(
            self, "Easy", screen_center_x - 100, screen_center_y - 25
            )
        self.hard_difficulty_button = Button(
            self, "Hard", screen_center_x - 100, screen_center_y + 100
            )
        
    def _save_high_score(self):
        """Write player high score into a file highscores.txt"""
        with open('python_work/alien_invasion/Chapter_13/ss_game_highscores.txt', 'w') as file:
            file.write(str(self.stats.high_score))
            file.close()
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._save_high_score()
                    sleep(0.5)
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos, event)     
                    self._check_easy_difficulty_button(mouse_pos, event)
                    self._check_hard_difficulty_button(mouse_pos, event)               
                    
    def _check_play_button(self, mouse_pos, event):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            # self.sounds.press_button_sound()
            self.settings.initialize_dynamic_settings()
            self._start_game()
            
    def _check_easy_difficulty_button(self, mouse_pos, event):
        """Star a new game with easy difficulty"""
        button_clicked = self.easy_difficulty_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Play sound of button clicked
            # self.sounds.press_button_sound()
            self.settings.easy_difficulty()
            self._start_game()
            
    def _check_hard_difficulty_button(self, mouse_pos, event):
        """Star a new game with easy difficulty"""
        button_clicked = self.hard_difficulty_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Play sound of button clicked
            # self.sounds.press_button_sound()
            self.settings.hard_difficulty()
            self._start_game()
            
    def _start_game(self):
        """Start a new game"""
        # Reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
            
        # Get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()
            
        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()
            
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
            
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            self._save_high_score()
            sleep(0.5)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
    
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
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self._start_new_level()
            
    def _start_new_level(self):
        """Start new level if fleet destroyed"""
        # Destroy existing bullets and create new fleet
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
            
        # Increase level
        self.stats.level += 1
        self.sb.prep_level()
        
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions of all
        aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
            # Look for aliens hitting the left of the screen
            self._check_aliens_left()
        
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
       
        if self.stats.ship_left > 0: 
            # Decrement ship_left, and update scoreboard
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            
            # Get red of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
        # Pause
        sleep(0.5)
        
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
            
    def _check_aliens_left(self):
        """Check if any aliens have reached the left of the screen"""
        for alien in self.aliens.sprites():
            if alien in self.aliens.sprites():
                if alien.rect.left <= 0:
                    
                    # Treat this the same as if the ship got hit
                    self._ship_hit()
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
        
        # Draw the score information
        self.sb.show_score()
        
        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_difficulty_button.draw_button()
            self.hard_difficulty_button.draw_button()
              
        # Make display visible        
        pygame.display.flip()
            
if __name__ == '__main__':
    # Making a game instance, and run the game
    sideway_shooter = SidewaysShooterPart2()
    sideway_shooter.run_game()