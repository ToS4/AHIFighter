import pygame, json, random, os
from Knight import Knight
from VampireGirl import VampireGirl
from LightningMage import LightningMage
from FireWizard import FireWizard
from AnimationController import Animation
import UI as UI
import HUD as HUD

pygame.init()

# fixed Screen
WIDTH = 1000
HEIGHT = 600

# Fullscreen
SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MAIN_WIDTH = SCREEN.get_width()
MAIN_HEIGHT = SCREEN.get_height()

# for scaling
scale_factor_width = MAIN_WIDTH / WIDTH
scale_factor_height = MAIN_HEIGHT / HEIGHT

pygame.display.set_caption("AHIF Fighter")

# Settings
settings = None
# open the file and save the data into settings (dictionary)
with open("settings.txt") as file:
    settings = json.loads(file.readline())

CLOCK = pygame.time.Clock()
FPS = 60

bg1 = pygame.image.load("src/assets/imgs/Backgrounds/bulkhead-wallsx3.png")
bg2 = pygame.image.load("src/assets/imgs/Backgrounds/country-platform.png")
bg3 = pygame.image.load("src/assets/imgs/Backgrounds/NightForest.png")

backgrounds = [bg1, bg2, bg3]
current_bg = backgrounds[random.randint(0,2)]

def select_character(name, player):

    y = 160

    pos = (800 if player == 2 else 200,y) # (x, y)
    scale_factor = (scale_factor_width, scale_factor_height)    #  (width_factor, height_factor)
    character_hitbox_size = (60,120)    # (width_hitbox, height_hitbox)
    flip = True if player == 2 else False
    controls = settings["player1"] if player == 1 else settings["player2"]

    if name == "Knight":

        files = []

        files.append((pygame.image.load("src/assets/imgs/Knight/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Knight/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Knight/Jump.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Knight/Attack1.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/Knight/Attack2.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/Knight/Attack3.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/Knight/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/Knight/Defend.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Knight/Dead.png").convert_alpha(),14))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return Knight( pos, scale_factor, character_hitbox_size, flip, controls, animations)
    
    elif name == "LightningMage":

        files = []

        files.append((pygame.image.load("src/assets/imgs/LightningMage/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Jump.png").convert_alpha(),7))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Dead.png").convert_alpha(),14))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Ability.png").convert_alpha(),6))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Attack1.png").convert_alpha(),5))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Attack2.png").convert_alpha(),10))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return LightningMage( pos, scale_factor, character_hitbox_size, flip, controls, animations)

    elif name == "FireWizard":

        files = []

        files.append((pygame.image.load("src/assets/imgs/FireWizard/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Jump.png").convert_alpha(),7))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Dead.png").convert_alpha(),14))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Ability.png").convert_alpha(),6))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Attack1.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Attack2.png").convert_alpha(),10))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return FireWizard( pos, scale_factor, character_hitbox_size, flip, controls, animations)

    elif name == "VampireGirl":

        files = []

        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Jump.png").convert_alpha(),7))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Dead.png").convert_alpha(),14))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Ability.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Attack1.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Attack2.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Attack3.png").convert_alpha(),10))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return VampireGirl( pos, scale_factor, character_hitbox_size, flip, controls, animations)


select_character_1 = "Knight"
select_character_2 = "VampireGirl"

player1 = select_character(select_character_1,1)
player2 = select_character(select_character_2,2)

healthbar_1 = HUD.Health_Bar(100 ,20, 250, 40, scale_factor_width, scale_factor_height)
healthbar_2 = HUD.Health_Bar(WIDTH-350, 20, 250, 40, scale_factor_width, scale_factor_height, True)

stamina_bar1 = HUD.Stamina_Bar(100,60,180,20,scale_factor_width, scale_factor_height)
stamina_bar2 = HUD.Stamina_Bar(WIDTH-280,60,180,20,scale_factor_width, scale_factor_height, True)

def game_loop():
    global player1, player2, current_bg
    running = True
    current_bg = pygame.transform.scale(current_bg, (MAIN_WIDTH,MAIN_HEIGHT))
    
    # import the reset variable from UI
    reset = UI.reset

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    UI.pause_menu(scale_factor_width, scale_factor_height, game_loop, settings)

        SCREEN.fill((255,255,255))
        SCREEN.blit(current_bg, (0,0))

        player1.handle_keys(SCREEN, MAIN_WIDTH, MAIN_HEIGHT, player2)
        player2.handle_keys(SCREEN, MAIN_WIDTH, MAIN_HEIGHT, player1)

        player1.update(SCREEN)
        player2.update(SCREEN)
        
        player1.draw(SCREEN)
        player2.draw(SCREEN)

        healthbar_1.draw(SCREEN, player1) 
        healthbar_2.draw(SCREEN, player2)

        stamina_bar1.draw(SCREEN,player1)
        stamina_bar2.draw(SCREEN,player2)

        if player1.health <= 0:
            player1 = select_character(select_character_1,1)
            player2 = select_character(select_character_2,2)
            #current_bg = backgrounds[random.randint(0,2)]
            UI.gameover_menu(scale_factor_width, scale_factor_height, game_loop, settings, "Player 2")
            current_bg = backgrounds[random.randint(0,2)]
            current_bg = pygame.transform.scale(current_bg, (MAIN_WIDTH,MAIN_HEIGHT))
        elif player2.health <= 0:
            player1 = select_character(select_character_1,1)
            player2 = select_character(select_character_2,2)
            #current_bg = backgrounds[random.randint(0,2)]
            UI.gameover_menu(scale_factor_width, scale_factor_height, game_loop, settings, "Player 1")
            current_bg = backgrounds[random.randint(0,2)]
            current_bg = pygame.transform.scale(current_bg, (MAIN_WIDTH,MAIN_HEIGHT))
        if reset:
            player1 = select_character(select_character_1,1)
            player2 = select_character(select_character_2,2)
            current_bg = backgrounds[random.randint(0,2)]
            current_bg = pygame.transform.scale(current_bg, (MAIN_WIDTH,MAIN_HEIGHT))
            reset = not reset
        CLOCK.tick(FPS)
        pygame.display.flip()

    pygame.quit()

UI.main_menu(scale_factor_width, scale_factor_height, game_loop, settings)