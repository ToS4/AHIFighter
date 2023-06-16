
##
# @file HUD.py
#
# @brief Creates classes necessary for the HUD
#
# @section desciption_HUD Description
# Defines a class for the following objects, that will be shown in-game:
# - Health_Bar (creates a health bar thats dependant on the players health)
# - Stamina_Bar (same goes for the Stamina_Bar)
# - Character_Icon (creates a rect with the selected character in it)
#
# @section libraries_HUD Libraries/Modules
# - pygame library (https://www.pygame.org/news)
#   - used for pretty much everything
# 
# @section author_HUD Author(s)
# - Created by mirko4001
# - Modified by mirko4001 & ToS4

import pygame

class Health_Bar():
    """! The Healthbar class

    Defines the players health bars which are dependant on the characters health
    """
    def __init__(self, pos_x, pos_y, width, height, scale_width, scale_height, r = False):
        """! Initializer for the Health_Bar class

        @param pos_x    Position on the x axis
        @param pos_y    Position on the y axis
        @param width    Width of the health bar
        @param height   height of the health bar
        @param scale_width  scale factor for the width
        @param scale_height scale factor for the height
        @param r        checks if the bar should be flipped
        """
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height

        self.scale_w = scale_width
        self.scale_h = scale_height

        self.reversed = r

    def draw(self, screen, player):
        """! Responsible for drawing the health_bar

        Draws 3 Rectangles: one for the outline, one for the red background and one for the green part

        @param screen   The screen which will be drawn on
        @param player   Which player is the health bar for
        """

        prozent = player.health / player.max_health
        pygame.draw.rect(screen, "Red", (self.x*self.scale_w, self.y*self.scale_h, (self.width*(player.max_health/100))*self.scale_w, self.height*self.scale_h))
        if not self.reversed:
            pygame.draw.rect(screen, "Green", (self.x*self.scale_w, self.y*self.scale_h, ((self.width*(player.max_health/100)) * prozent)*self.scale_w, self.height*self.scale_h))
        else:
            pygame.draw.rect(screen, "Green", ((self.x-(self.width*prozent)+250)*self.scale_w, self.y*self.scale_h,
                                                (((self.width*(player.max_health/100)) * prozent)+2)*self.scale_w, self.height*self.scale_h))
        pygame.draw.rect(screen,"black",(self.x*self.scale_w, self.y*self.scale_h, (self.width*(player.max_health/100))*self.scale_w, self.height*self.scale_h), 1)

class Stamina_Bar():
    """! The Stamina_Bar class

    It is similiar to the health bar and uses the stamina of the characters
    """

    def __init__(self, x,y,w,h,scale_w,scale_h, r = False):
        """! Initializer for the Stamina_Bar class

        @param x    Position on the x axis
        @param y    Position on the y axis
        @param w    Width of the stamina bar
        @param h    height of the stamina bar
        @param scale_w  scale factor for the width
        @param scale_h  scale factor for the height
        @param r    checks if the bar should be flipped
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.scale_w = scale_w
        self.scale_h = scale_h

        self.reversed = r

    def draw(self, screen, player):
        """! Draws the stamina bar

        Draws 2 Rectangles: one for the outline and one for the blue color
        If it is reversed, the blue bar will draw and moved to a correct position, giving an illusion that it is flipped

        @param screen   The screen which will be drawn on
        @param player   Which player is the stamina bar for
        """
        prozent = player.stamina / player.max_stamina
        if not self.reversed:
            pygame.draw.rect(screen, "lightblue", (self.x*self.scale_w, self.y*self.scale_h, (self.w * prozent)*self.scale_w, self.h*self.scale_h))
            pygame.draw.rect(screen,"black",(self.x*self.scale_w, self.y*self.scale_h, self.w*self.scale_w, self.h*self.scale_h), 1)
        else:
            pygame.draw.rect(screen, "lightblue", ((self.x-(self.w * prozent)+180)*self.scale_w, self.y*self.scale_h,
                                                    ((self.w * prozent)+2)*self.scale_w, self.h*self.scale_h))
            pygame.draw.rect(screen,"black",((self.x-1)*self.scale_w, self.y*self.scale_h, (self.w+1)*self.scale_w, self.h*self.scale_h), 1)
            
class Character_Icon():
    """! The Character_Icon class

    This will create a box and the character icon in it, which will be visible in the HUD in-game
    """
    def __init__(self, x,y,w,h, scale_w, scale_h):
        """! Initializer for Character_Icon class

        @param x    Position on the x axis
        @param y    Position on the y axis
        @param w    Width of the box
        @param h    height of the box
        @param scale_w  scale factor for the width
        @param scale_h  scale factor for the height
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.scale_w = scale_w
        self.scale_h = scale_h

        self.rect = pygame.Rect(self.x*self.scale_w, self.y*self.scale_h, self.w*self.scale_w, self.h*self.scale_h)

    def draw(self, screen, char):
        """! Draws the Icon and the rect

        @param screen   The screen which will be drawn on
        @param char     Which character is selected
        """
        # the picture of the character
        icon = pygame.image.load(f"src/assets/imgs/{char}/Icon.png")
        icon = pygame.transform.scale(icon, (99*self.scale_w,99*self.scale_h))

        # draw rect for black outline and rect for white fill
        pygame.draw.rect(screen, "darkolivegreen1", self.rect)
        pygame.draw.rect(screen, "black", self.rect, 3)
        screen.blit(icon, self.rect)