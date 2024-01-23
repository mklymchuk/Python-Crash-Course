import pygame.mixer

class MusicAndSound:
    """Handle music and sound in game"""
    
    def __init__(self):
        """Resource initialization"""
        pygame.mixer.init()
        
        
    def play_background_music(self):
        """Play background music before player press play button"""
        self.main_theme = pygame.mixer.music.load(
            'python_work/alien_invasion/sounds/main_theme.wav'
            )
        pygame.mixer.music.play(loops=-1, fade_ms=2000)
        
    def unload_background_music(self):
        """Unload background music"""
        pygame.mixer.music.unload()
        
    def press_button_sound(self):
        """Sound plays when player press button"""
        self.button_sound = pygame.mixer.Sound(
            'python_work/alien_invasion/sounds/press_button_sound.wav'
        )
        self.button_sound.play()
        
    def play_collision_sound(self):
        """Sound of collision between aliens and ship, 
        and when aliens reach the bottom of the screen"""
        self.collision_sound = pygame.mixer.Sound(
            'python_work/alien_invasion/sounds/collision_alien_ship_or_bottom.wav'
        )
        self.collision_sound.play()
        
    def bullet_hit_aliens(self):
        """Sound when bullet hit aliens"""
        self.bullet_hit_sound = pygame.mixer.Sound(
            'python_work/alien_invasion/sounds/bullet_hit_aliens.wav'
        )
        self.bullet_hit_sound.play()

    def play_quit_sound(self):
        """Play sound when player quit game"""
        self.exit_sound = pygame.mixer.Sound(
            'python_work/alien_invasion/sounds/exit_sound.wav'
        )
        self.exit_sound.play()