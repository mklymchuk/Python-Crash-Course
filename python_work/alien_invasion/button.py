import pygame.font

class Button:
    
    def __init__(self, ai_game, msg, x_offset, y_offset):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) # type: ignore
        
        # Build the button's rect object and center it
        self.rect = pygame.Rect(x_offset + 0, y_offset + 0, self.width, self.height)
        #self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turns msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect(center = self.rect.center)
        # self.msg_image_rect.center = self.rect.center       
        
    def draw_button(self):
        # Draw black button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)