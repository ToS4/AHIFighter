
##
# @file ButtonController.py
#
# @brief Defines classes necessary for the buttons and controls
#
# @section description_ButtonController Description
# Defines a class for objects used to control the game (hotkeys, ...):
# - Button (used to make buttons for the UI)
# - InputBox (used to save inputs in a box)
# - CharacterBox (creates a box with the character in it)
#
# @section libraries_ButtonController Libraries/Modules
# - pygame library (https://www.pygame.org/news)
# - pygame.gfxdraw (used for advanced drawing)
# 
# @section author_HUD Author(s)
# - Created by mirko4001
# - Modified by mirko4001 & ToS4

import pygame
import pygame.gfxdraw

class Button:
    """! The Button class

    Creates a Button that has a hover effect and can do an action if it is clicked
    """
    def __init__(self, pos_x, pos_y, width, height, color, text, text_color, font, scale_width, scale_height, action = None):
        """! Initializer for the Button class

        @param pos_x    Position on the x axis
        @param pos_y    Position on the y axis
        @param width    Width of the button
        @param height   Height of the button
        @param color    Color of the button
        @param text     Text that is centered in the button
        @param text_color   Color of the displayed text
        @param font     Size and font of the text
        @param scale_width  Scale factor for the width
        @param scale_height Scale factor for the height
        @param action   What happens when the button is clicked
        """
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.action = action
        self.rect = pygame.Rect(pos_x * scale_width, pos_y * scale_height, width * scale_width, height * scale_height)

    def draw(self, screen):
        """! Responsible for drawing the Button

        @param screen   The screen which will be drawn on
        """
        pygame.draw.rect(screen, self.color, self.rect)
        font_surface = self.font.render(self.text, True, self.text_color)
        font_rect = font_surface.get_rect()
        font_rect.center = self.rect.center
        screen.blit(font_surface, font_rect)

    def handle_event(self, event):
        """! Responsible for the action, when the button is pressed

        @param event    Keycode from Pygame
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action != None:
                    self.action()
    
    def hover_effect(self, mouse_pos):
        """! Makes the button different when it is hovered

        @param mouse_pos    Position of the mouse
        """
        mouse_x, mouse_y = mouse_pos
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.text_color = "Green"
        else:
            self.text_color = "White"

class InputBox:
    """! The InputBox class

    Creates a box that can save text in a box
    """
    def __init__(self, x, y, w, h, font, text_color, color, scale_width, scale_height, settings, text = "") -> None:
        """! Initializer for InputBox class

        @param x    Position on the x axis
        @param y    Position on the y axis
        @param w    Width of the box
        @param h   Height of the box
        @param font     Size and font of the text
        @param text_color   Color of the displayed text
        @param color    Color of the box
        @param scale_width  Scale factor for the width
        @param scale_height Scale factor for the height
        @param settings The saved settings in the settings.txt
        @param text     Text that is centered in the box
        """
        self.color_tmp = color
        self.color_a = 255
        self.color = pygame.Color(*color, self.color_a)

        self.active = False

        self.scale_height = scale_height
        self.scale_width = scale_width

        self.rect = pygame.Rect(x*scale_width,y*scale_height,w*scale_width,h*scale_width)
        
        self.settings = settings

        self.font = font
        self.user_text = text
        self.text_color = text_color

    def draw(self, screen):
        """! Draws the InputBox

        @param screen   The screen which will be drawn on
        """
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
        """! Responsible for the action, when the button is pressed

        @param event    Keycode from Pygame
        """
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

class CharacterBox:
    """! The CharacterBox class

    Creates a Rectangle with the player in it, for the selection
    """
    def __init__(self, x,y,w,h, color, scale_width, scale_height, char):
        """! Initializer for the CharacterBox class

        @param x    Position on the x axis
        @param y    Position on the y axis
        @param w    Width of the box
        @param h    Height of the box
        @param scale_width  Scale factor for the width
        @param scale_height Scale factor for the height
        @param char The selected character
        """
        self.rect = pygame.Rect(x*scale_width, y*scale_height, w*scale_width, h*scale_height)
        self.color = color
        self.scale_w = scale_width
        self.scale_h = scale_height

        self.char = char
        self.selected = False

    def draw(self, screen):
        """! Draws the Box

        2 rects: 1 for the outline and 1 for the inside color

        @param screen   The screen which will be drawn on
        """
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, 2)
                
    def select(self,char_list, char):
        """! Changes color of the box, when it is selected

        @param char_list    A dictionary which has every character and its theme color in it
        @param char         The selected character
        """
        self.color = char_list[char]