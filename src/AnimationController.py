"""! @brief Animation Controller"""

##
# @file AnimationController.py
#
# @brief Animation
#
# @section description_animation Description
# - a class for creating animation with their own update funciton to handle everything
#
# @section libraries_animation Libraries/Modules
# - pygame
#
# @section author_animation Author(s)
# - Created by ToS4
# - Modified  by mirko4001 & ToS4
#
##

import pygame

class Animation:
    """! Animation Class"""

    def __init__(self, sprite_sheet, frame_width, frame_height, frame_duration):
        """! Initializes the Animation.
        
            @param self the animation class
            @param sprite the loaded sprite using pygame
            @param frame_width    image width
            @param frame_height   image height
            @param frame_duration   how long frames each images takes
        """

        self.sprite_sheet = sprite_sheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_duration = frame_duration
        self.frames = []
        self.current_frame = 0
        self.frame_counter = 0

        self.load_frames()

    def load_frames(self):
        """! Load Frames
        
            @param self the animation class

            cuts the sprite-sheet and saves all images in a list
        """

        sheet_width = self.sprite_sheet.get_width()
        sheet_height = self.sprite_sheet.get_height()
        rows = sheet_height // self.frame_height
        cols = sheet_width // self.frame_width

        for row in range(rows):
            for col in range(cols):
                x = col * self.frame_width
                y = row * self.frame_height
                frame = self.sprite_sheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))
                self.frames.append(frame)

    def update(self):
        
        """! Update
        
            @param self the animation class

            updates the animation to the next image
        """

        self.frame_counter += 1
        if self.frame_counter >= self.frame_duration:
            self.frame_counter = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0

    def get_image(self):
        """! Get Image
        
            @param self the animation class

            @return the current image
        """

        return self.frames[self.current_frame]