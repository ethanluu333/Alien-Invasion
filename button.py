import pygame.font
PURPLE = (102, 0, 204)
MAROON = (153, 0, 76)
BLUE = (153, 153, 255)
PINK = (255, 153, 255)

class Button():
    def __init__(self, screen, msg, ul):
        self.screen = screen

        self.width, self.height = 220, 50
        self.colors = [BLUE, PINK]
        self.color_idx = 0
        self.color = self.colors[self.color_idx]
        self.color = MAROON
        self.text_color = PURPLE
        self.font = pygame.font.Font("font/gameFont.otf", 40)
        self.ul = ul

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left, self.rect.top = ul[0], ul[1]
        
        self.msg = msg
        self.image = self.font.render(self.msg, True, self.text_color, self.color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center

    def toggle_colors(self): 
        self.color_idx += 1
        self.color_idx %= 2
        self.draw()
    
    def draw(self):
        color = self.colors[self.color_idx]
        self.image = self.font.render(self.msg, True, self.text_color, color)
        self.screen.fill(color, self.rect)
        self.screen.blit(self.image, self.image_rect)
