
##
# @file LightningMage.py
#
# @brief Lightning Mage Character
#
# @section description_lm Description
# - the lightning mage class
#
# @section libraries_lm Libraries/Modules
# - pygame
# - time
# - threading
# - hitboxcontroller (local)
#
# @section author_lm Author(s)
# - Created by ToS4
# - Modified  by mirko4001 & ToS4
#
#

import pygame, time,threading
from HitboxController import Hitbox

class LightningMage():
    """! Lightning Mage"""

    def __init__(self, pos: tuple, scale_factor: tuple, character_hitbox_size: tuple, flip : bool, controls: dict, animations: list):
        """! Initializes the Character.
        
            @param self the client, a class object of their selected character
            @param pos  the position of the character's hitbox, a tuple with x- and y-axis
            @param character_hitbox_size    the width and height of the hitbox
            @param flip   the character flip state at the start
            @param controls   the settings keys
            @param animations   a matrix with all the animations, each action has its own list with all the images saved
        """

        self.Name = "LightingMage"

        self.x, self.y = pos
        self.width_factor, self.height_factor = scale_factor
        self.width_hitbox, self.height_hitbox = character_hitbox_size

        self.jumping = False
        self.attacking = False
        self.running = False

        self.rect = pygame.Rect((self.x*self.width_factor,self.y*self.height_factor, self.width_hitbox*self.width_factor, self.height_hitbox*self.height_factor))

        self.max_health = 100
        self.health = self.max_health

        self.speed = 6 * self.width_factor
        self.jump_power = 22 * self.height_factor

        self.gravity_y = 0
        self.gravity_x = 0
        self.flip = flip

        self.settings = controls

        self.animations = animations
        self.old_action = 0
        self.action = 0
        self.image = 0

        self.attack_cooldown = 0
        self.attack_index = 0
        self.attack_hit = 0
        self.hit = 0

        self.knockback = 20 * self.width_factor
        self.damage = 7

        self.using = False
        self.max_stamina = 20
        self.stamina = self.max_stamina
        self.stamina_need = self.max_stamina
        self.ability_damage = self.damage * 3
        self.ability_frames = 0

    def handle_keys(self, SCREEN, WIDTH, HEIGHT, target):
        """! Key-Handler of the Character

            @param self the client, a class object of their selected character
            @param SCREEN   the pygame screen object
            @param WIDTH    the width of the screen
            @param HEIGHT   the height of the screen
            @param target   the target, a class object of their selected character
            """

        GRAVITY = 2
        keys = pygame.key.get_pressed()

        delta_x = 0
        delta_y = 0

        new_action = 0

        if not self.attacking and not self.using:
            if self.hit <= 0:
                if keys[self.settings["left"]]:
                    delta_x = -self.speed
                    new_action = 1

                if keys[self.settings["right"]]:
                    delta_x = self.speed
                    new_action = 1

                if keys[self.settings["jump"]] and not self.jumping and not self.using:
                    self.gravity_y -= self.jump_power
                    self.jumping = True
                
                if keys[self.settings["attack"]] and not self.jumping and not self.using:
                    self.attack(SCREEN, target)

                if keys[self.settings["ability"]] and not self.jumping and not self.using:
                    self.ability(SCREEN,target)

        else:
            new_action = 6 + self.attack_index

        if not self.using and self.stamina < self.max_stamina and self.hit <= 0:
            self.stamina += 1/60

        self.gravity_y += GRAVITY
        delta_y += self.gravity_y

        if self.gravity_x > 0:       
            self.gravity_x -= GRAVITY
        else:
            self.gravity_x = 0

        if self.flip:
            delta_x += self.gravity_x
        else:
            delta_x -= self.gravity_x

        if self.rect.left + delta_x < 0:
            delta_x = -self.rect.left
            self.gravity_x = 0
        if self.rect.right + delta_x > WIDTH:
            delta_x = WIDTH - self.rect.right
            self.gravity_x = 0
        if self.rect.bottom + delta_y > HEIGHT - self.y:
            self.gravity_y = 0
            self.jumping = False
            delta_y = HEIGHT - self.y - self.rect.bottom

        if self.jumping:
            new_action = 2
        
        if self.ability_frames >= 6 * 12: # duration of each image is x frames and there is a total of 12 images (see main.py)
            self.ability_frames = 0
            self.using = False
    
        if self.using:
            new_action = 5
            self.ability_frames += 1

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        self.rect.x += delta_x
        self.rect.y += delta_y
        self.old_action = self.action
        self.action = new_action

    def update(self, SCREEN):
        """! Update of the Character

            @param self the client, a class object of their selected character
            @param SCREEN   the pygame screen object
            """
        
        if self.attacking: 
            if time.time() - self.attack_cooldown > 0.9:
                self.attack_cooldown = 0
                self.attacking = False

        if self.hit > 0:
            self.hit -= 1/60
            if not self.using:
                self.action = 3
        else:
            self.hit = 0

        if self.old_action != self.action:
            for animation in self.animations:
                animation.frame_counter = 0
                animation.current_frame = 0

        self.animations[self.action].update()
        self.image = self.animations[self.action].get_image()

    def attack(self,SCREEN, target):
        """! Attack Function of the Character (gets fires once clicking a hotkey)

            @param self the client, a class object of their selected character
            @param SCREEN   the pygame screen object
            @param target   the target, a class object of their selected character
            """
        
        if not self.attacking and not self.using:
            self.attacking = True
            if time.time() - self.attack_hit < 1.1:
                self.attack_index += 1
            else:
                self.attack_index = 0

            self.attack_index = self.attack_index % 2
            self.attack_hit = time.time()
            self.attack_cooldown = time.time()

            self.action = 6 + self.attack_index

            def check():
                if Hitbox((-25 if self.flip else +25 ,0),(self.width_factor,self.height_factor),self,1,1).detect_collision(SCREEN, target):

                    target.hit = 1
                    target.gravity_y = 0

                    t = 0

                    if self.attack_index == 0:
                        t = 1/60*8*3.8
                    elif self.attack_index == 1:
                        t = 1/60*8*4

                    time.sleep(t)
                    

                    if target.Name == "Samurai" and target.using:
                        target.stamina -= self.damage
                        if target.max_stamina <= 0:
                            target.health -= self.damage * 1.5
                            target.stamina = 0
                    else:
                        target.health -= self.damage

                    if self.attack_index == 1:
                        target.gravity_x = self.knockback

            

            threading.Thread(target=check).start()

    def ability(self,SCREEN,target):
        """! Ability Function of the Character (gets fires once clicking a hotkey)

            @param self the client, a class object of their selected character
            @param SCREEN   the pygame screen object
            @param target   the target, a class object of their selected character
            """
        
        if not self.using and not self.attacking:
            if self.stamina >= self.stamina_need:
                self.stamina -= self.stamina_need

                self.action = 5
                self.using = True

                def check():
                    if Hitbox((-50 if self.flip else +30 ,0),(self.width_factor,self.height_factor),self,1,1.8).detect_collision(SCREEN, target):

                        target.hit = 1.5
                        target.gravity_y = 0

                        t = 1/60*12*6

                        time.sleep(t)
                        

                        if target.Name == "Samurai" and target.using:
                            target.stamina -= self.ability_damage
                            if target.stamina <= 0:
                                target.health -= self.ability_damage * 0.2
                                target.stamina = 0
                        else:
                            target.health -= self.ability_damage

                        target.gravity_x = self.knockback


                

                threading.Thread(target=check).start()

    def draw(self, SCREEN):
        """! Draw Function of the Character

            @param self the client, a class object of their selected character
            @param SCREEN   the pygame screen object
            """
        
        pygame.draw.rect(SCREEN, (0,255,0), self.rect)
        img = pygame.transform.scale(pygame.transform.flip(self.image, self.flip, False), (self.width_hitbox*3.5*self.width_factor, self.height_hitbox*2*self.height_factor))
        img_rect = img.get_rect()
        if not self.flip:
            img_rect.bottomleft = self.rect.bottomleft
            img_rect.x -= 58 * self.width_factor
            if self.using:
                img_rect.x += 50 * self.width_factor
        else:
            img_rect.bottomright = self.rect.bottomright
            img_rect.x += 58 * self.width_factor
            if self.using:
                img_rect.x -= 50 * self.width_factor
        
        SCREEN.blit(img, img_rect)