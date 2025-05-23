import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from music_and_sound import MusicAndSound
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        # Create an instance to store game statistics, and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.sounds = MusicAndSound()
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Set the background color.
        self.bg_color = (230, 230, 230)
        
        self.buttons_initialization()
        
    def run_game(self):
        """Start the main loop for the game."""
        # Play game theme
        self.sounds.play_background_music()
        
        while True:
            self._check_events()
                
            if self.stats.game_active:
                self.sounds.unload_background_music()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_aliens_bottom()
                
            self._update_screen()
            
    def _start_game(self):
        """Start and reset game"""
        
        # Reset the game statistic
        self.stats.reset_stats()
        self.stats.game_active = True
          
        # Get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()
          
        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()
        
    def buttons_initialization(self):
        """Button initialization"""
        # Make the Play button
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
        with open('python_work/alien_invasion/highscores.txt', 'w') as file:
            file.write(str(self.stats.high_score))
            file.close()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._save_high_score()
                self.sounds.play_quit_sound()
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
                
    def _start_new_game(self):
        """Start a new game."""
        self._start_game()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
                
    def _check_easy_difficulty_button(self, mouse_pos, event):
        """Star a new game with easy difficulty"""
        button_clicked = self.easy_difficulty_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Play sound of button clicked
            self.sounds.press_button_sound()
            self.settings.easy_difficulty()
            self._start_new_game()
            
    def _check_hard_difficulty_button(self, mouse_pos, event):
        """Star a new game with easy difficulty"""
        button_clicked = self.hard_difficulty_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Play sound of button clicked
            self.sounds.press_button_sound()
            self.settings.hard_difficulty()
            self._start_new_game()
                
    def _check_play_button(self, mouse_pos, event):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Play sound of button clicked
            self.sounds.press_button_sound()
            self.settings.initialize_dynamic_settings()
            self._start_new_game()
                
    def _check_keydown_events(self, event):
        """Respond keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._save_high_score()
            self.sounds.play_quit_sound()
            sleep(0.5)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
            
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update position
        self.bullets.update()
            
        # Get rid of bullets that have dissappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))
        
        self._check_bullet_alien_collisions()
        
    def _start_new_level(self):
        """Start new level if fleet destroyed"""
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
            
        # Increase level
        self.stats.level += 1
        self.sb.prep_level()
                
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
            )
        if collisions:
            for aliens in collisions.values():
                self.sounds.bullet_hit_aliens()
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.aliens:
            self._start_new_level()
        
    def _update_aliens(self):
        """Check if the fleet is at an edge,
        then update the position of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update() 
        
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
            # Look for aliens hitting the bottom of the screen
            self._check_aliens_bottom()
            
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ship_left > 0:
            # Decrement ships_left, and update scoreboard
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            
            # Play sound of collision
            self.sounds.play_collision_sound()
            
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create the new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
        # Pause
        sleep(0.5)
        
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width) 
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)      
    
    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in the row.
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)
            
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                
                #Play sound of collision
                self.sounds.play_collision_sound()
                break
                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
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
        
        pygame.display.flip()
        
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()        