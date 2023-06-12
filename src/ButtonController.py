import pygame
import pygame.gfxdraw
class Button:
    def __init__(self, pos_x, pos_y, width, height, color, text, text_color, font, scale_width, scale_height, action = None):
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.action = action
        self.rect = pygame.Rect(pos_x * scale_width, pos_y * scale_height, width * scale_width, height * scale_height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font_surface = self.font.render(self.text, True, self.text_color)
        font_rect = font_surface.get_rect()
        font_rect.center = self.rect.center
        screen.blit(font_surface, font_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action != None:
                    self.action()
    
    def hover_effect(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.text_color = "Green"
        else:
            self.text_color = "White"

class InputBox:
    def __init__(self, x, y, w, h, font, text_color, color, scale_width, scale_height, settings, player, text = "") -> None:
        self.color_tmp = color
        self.color_a = 255
        self.color = pygame.Color(*color, self.color_a)

        self.active = False

        self.scale_height = scale_height
        self.scale_width = scale_width

        self.rect = pygame.Rect(x*scale_width,y*scale_height,w*scale_width,h*scale_width)
        
        self.settings = settings
        self.player = player

        self.font = font
        self.user_text = text
        self.text_color = text_color

    def draw(self, screen):        
        text_surface = self.font.render(self.user_text, True, self.text_color)

        if self.active:
            self.color_a = 255
            self.color = (*self.color_tmp, self.color_a)
        else:
            self.color_a = 50
            self.color = (*self.color_tmp, self.color_a)

        # diese .gfxdraw ist einfach ein .draw mit besseren Eigenschaften
        pygame.gfxdraw.box(screen, self.rect, self.color)
        pygame.draw.rect(screen, "black", self.rect, 2)
        screen.blit(text_surface, (self.rect.x+24*self.scale_width, self.rect.y+10*self.scale_height))
        self.rect.w = max(100, text_surface.get_width()+self.scale_height*50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = ""
            elif event.key == pygame.K_RETURN:
                self.active = False
            else:
                check = False
                for i in self.settings["player2"].values():
                    if event.key == i:
                        check = True
                for i in self.settings["player1"].values():
                    if event.key == i:
                        check = True
                if not check:
                    self.user_text = ""
                    self.user_text += pygame.key.name(event.key)
                    self.active = False
        return self.user_text
    
    def hover_effect(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.color_a = 50
            self.color = (*self.color_tmp, self.color_a)
        else:
            self.color_a = 250
            self.color = (*self.color_tmp, self.color_a)

class CharacterBox:
    def __init__(self, x,y,w,h, color, scale_width, scale_height, char):
        self.rect = pygame.Rect(x*scale_width, y*scale_height, w*scale_width, h*scale_height)
        self.color = color

        self.char = char

    def draw(self, screen):
        # 2 rects: 1 for the outline and 1 for the inside color
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, 2)
        
    def select(self):
        self.color = "grey"