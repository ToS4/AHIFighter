import pygame
import sys

class Health_Bar():
    def __init__(self, pos_x, pos_y, width, height, scale_width, scale_height, r = False):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height

        self.scale_w = scale_width
        self.scale_h = scale_height

        self.reversed = r

    def draw(self, screen, player):
        # 3 rects: outline, red and green
        prozent = player.health / player.max_health
        pygame.draw.rect(screen, "Red", (self.x*self.scale_w, self.y*self.scale_h, self.width*self.scale_w, self.height*self.scale_h))
        if not self.reversed:
            pygame.draw.rect(screen, "Green", (self.x*self.scale_w, self.y*self.scale_h, (self.width * prozent)*self.scale_w, self.height*self.scale_h))
        else:
            pygame.draw.rect(screen, "Green", ((self.x-(self.width*prozent)+250)*self.scale_w, self.y*self.scale_h,
                                                ((self.width * prozent)+2)*self.scale_w, self.height*self.scale_h))
        pygame.draw.rect(screen,"black",(self.x*self.scale_w, self.y*self.scale_h, self.width*self.scale_w, self.height*self.scale_h), 1)

class Stamina_Bar():
    def __init__(self, x,y,w,h,scale_w,scale_h, r = False):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.scale_w = scale_w
        self.scale_h = scale_h

        self.reversed = r

    def draw(self, screen, player):
        prozent = player.stamina / player.max_stamina
        if not self.reversed:
            pygame.draw.rect(screen, "lightblue", (self.x*self.scale_w, self.y*self.scale_h, (self.w * prozent)*self.scale_w, self.h*self.scale_h))
            pygame.draw.rect(screen,"black",(self.x*self.scale_w, self.y*self.scale_h, self.w*self.scale_w, self.h*self.scale_h), 1)
        else:
            pygame.draw.rect(screen, "lightblue", ((self.x-(self.w * prozent)+180)*self.scale_w, self.y*self.scale_h,
                                                    ((self.w * prozent)+2)*self.scale_w, self.h*self.scale_h))
            pygame.draw.rect(screen,"black",((self.x-1)*self.scale_w, self.y*self.scale_h, (self.w+1)*self.scale_w, self.h*self.scale_h), 1)
            
class Character_Icon():
    def __init__(self, x,y,w,h, scale_w, scale_h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.scale_w = scale_w
        self.scale_h = scale_h

        self.rect = pygame.Rect(self.x*self.scale_w, self.y*self.scale_h, self.w*self.scale_w, self.h*self.scale_h)

    def draw(self, screen, char):
        # the picture of the character
        icon = pygame.image.load(f"src/assets/imgs/{char}/Icon.png")
        icon = pygame.transform.scale(icon, (99*self.scale_w,99*self.scale_h))

        # draw rect for black outline and rect for white fill
        pygame.draw.rect(screen, "darkolivegreen1", self.rect)
        pygame.draw.rect(screen, "black", self.rect, 3)
        screen.blit(icon, self.rect)