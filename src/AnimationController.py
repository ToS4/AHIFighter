import pygame

class Animation:
    def __init__(self, sprite_sheet, frame_width, frame_height, frame_duration):
        self.sprite_sheet = sprite_sheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_duration = frame_duration
        self.frames = []
        self.current_frame = 0
        self.frame_counter = 0

        self.load_frames()

    def load_frames(self):
        
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
        self.frame_counter += 1
        if self.frame_counter >= self.frame_duration:
            self.frame_counter = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0

    def get_image(self):
        return self.frames[self.current_frame]