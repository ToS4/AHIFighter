import pygame

class Hitbox():

    def __init__(self, pos: tuple, scale_factor: tuple, player: object, y_factor = 1, x_factor = 1):

        self.x, self.y = pos
        self.width_factor, self.height_factor = scale_factor
        #self.width_hitbox, self.height_hitbox = hitbox_size

        #self.rect = pygame.Rect((self.x*self.width_factor,self.y*self.height_factor, self.width_hitbox*self.width_factor, self.height_hitbox*self.height_factor))

        self.rect = pygame.Rect(self.x + player.rect.centerx - (1.5 * player.rect.width * player.flip), self.y + player.rect.y, 1.5 * x_factor * player.rect.width, y_factor * player.rect.height)

    def detect_collision(self,SCREEN,target):
        pygame.draw.rect(SCREEN, (0,255,0), self.rect)
        if self.rect.colliderect(target.rect):
            return True
        return False