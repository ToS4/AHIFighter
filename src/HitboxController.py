##
# @file HitboxController.py
#
# @brief Hitbox Controller
#
# @section description_hitbox Description
# - a class for creating hitboxes and handling them
#
# @section libraries_hitbox Libraries/Modules
# - pygame
#
# @section author_hitbox Author(s)
# - Created by ToS4
# - Modified  by mirko4001 & ToS4
#
#

import pygame

class Hitbox():
    """! Hitbox Class"""

    def __init__(self, pos: tuple, scale_factor: tuple, player: object, y_factor = 1, x_factor = 1):
        """! Initializes the Hitbox.
        
            @param self the animation class
            @param pos the x-,y-axis offest from the center of the player rect
            @param scale_factor scale factor of the hitbox to get it bigger or small 
            @param frame_height   image height
            @param frame_duration   how long frames each images takes
        """

        self.x, self.y = pos
        self.width_factor, self.height_factor = scale_factor
        #self.width_hitbox, self.height_hitbox = hitbox_size

        #self.rect = pygame.Rect((self.x*self.width_factor,self.y*self.height_factor, self.width_hitbox*self.width_factor, self.height_hitbox*self.height_factor))

        self.rect = pygame.Rect(self.x + player.rect.centerx - (1.5 * player.rect.width * player.flip), self.y + player.rect.y, 1.5 * x_factor * player.rect.width, y_factor * player.rect.height)

    def detect_collision(self,SCREEN,target):
        """! Detect Collision
        
            @param self the animation class
            @param SCREEN the screen object (from pygame)
            @param target the target class
        """
        pygame.draw.rect(SCREEN, (0,255,0), self.rect)
        if self.rect.colliderect(target.rect):
            return True
        return False