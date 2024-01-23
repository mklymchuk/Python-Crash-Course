import pygame.font

class Button:
    
    def __init__(self, tp_game, msg):
        """Initialize button attributes"""
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set font
        self.font = pygame.font.SysFont('Apple SD Gothic Neo UltraLight', 48)
        
        # Build the button rect object and center it
        self.button_rect = pygame.Rect(
            0, 0, tp_game.settings.width, tp_game.settings.height
            )
        self.button_rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once
        self._prep_msg(msg, tp_game)
        
    def _prep_msg(self, msg, tp_game):
        """Turns message into a rendered image and center text on the button"""
        self.msg_image = self.font.render(
            msg, True, tp_game.settings.text_color, tp_game.settings.button_color
            )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center
            
    def draw_button(self, tp_game):
        # Draw black button and then draw message
        self.screen.fill(tp_game.settings.bullet_color, self.button_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)        