import sys
from time import sleep

import pygame

from target_practice_14_2_settings import Settings
from target_practice_14_2_game_stats import GameStats
from target_practice_14_2_ship import Ship
from target_practice_14_2_button import Button
from target_practice_14_2_target import Target
from target_practice_14_2_bullet import Bullet

class TargetPractice:
    """A target practice game, where a player shoots a rectangle, and if he 
    misses three times - game ends"""
    
    def __init__(self):
        """Game initialization, and resourse load"""
        pygame.init()
        
        self.settings = Settings()
        self.stats = GameStats(self)
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Target practice")
        
        self.ship = Ship(self)
        
        self.target = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        # Create an instance of the Target class and add it to the target group
        target = Target(self)
        self.target.add(target)
        
        # Make the play button
        self.play_button = Button(self, "Play")
        
        # Start target practice game in false state
        self.game_active = False
        pygame.mouse.set_visible(True)
        
    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self.target.sprites()[0].move_target()
                self.bullets.update()
            
            self._update_screen()
            
            pygame.display.flip()
            
    def _check_events(self):
        """Key and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self.settings.reset_game_speed()
                
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.button_rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game statistics
            self.stats.reset_stats()
            self.settings.players_life = 3
            self.stats.game_active = True

            #Get rid of any remaining aliens and bullets
            self.bullets.empty()
            
            # Center ship
            self.ship.center_ship()
            
            # Hide the mouse cursor
            pygame.mouse.set_visible(False)
            
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
                            
    def _check_keyup_events(self, event):
        """Respond to keyreleases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def fire_bullet(self):
        """Create a new bullet, and add it to the group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update() 
            
        # Get rid of old bullets
        for bullet in self.bullets.copy():
            if pygame.sprite.spritecollideany(self.target.sprites()[0], self.bullets):
                self.bullets.remove(bullet)
                self.settings.bullet_collide += 1
                print(self.settings.bullet_collide)
                if self.settings.bullet_collide >= 10:
                    self.settings.target_increase_speed()
                    self.settings.bullet_collide = 0
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self._update_player_life()
                
    def _update_player_life(self):
        """Check if bullet misses the target, and update player life"""
        if self.settings.players_life > 0:
            # Decrement player's life
            self.settings.players_life -= 1

            # Center the ship
            self.ship.center_ship()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        # Pause
        sleep(0.5)
            
    def _update_screen(self):
        """Update screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.target.sprites()[0].draw_target()       
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # Draw the play button only if the game is not active
        if not self.stats.game_active:
            self.play_button.draw_button(self)
            
        pygame.display.flip()
            
if __name__ == '__main__':
    """Making an instance of Target Practice"""
    target_practice = TargetPractice()
    target_practice.run_game()