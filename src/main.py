import pygame, json, random, os
import UI
import HUD

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

healthbar_1 = HUD.Health_Bar(100 ,20, 250, 40, scale_factor_width, scale_factor_height)
healthbar_2 = HUD.Health_Bar(WIDTH-350, 20, 250, 40, scale_factor_width, scale_factor_height, True)

stamina_bar1 = HUD.Stamina_Bar(100,60,180,20,scale_factor_width, scale_factor_height)
stamina_bar2 = HUD.Stamina_Bar(WIDTH-280,60,180,20,scale_factor_width, scale_factor_height, True)

def game_loop(player1, player2):
    global current_bg
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
            player1 = UI.select_character(UI.select_p1,1, settings)
            player2 = UI.select_character(UI.select_p2,2, settings)
            #current_bg = backgrounds[random.randint(0,2)]
            UI.gameover_menu(scale_factor_width, scale_factor_height, game_loop, settings, "Player 2")
            current_bg = backgrounds[random.randint(0,2)]
            current_bg = pygame.transform.scale(current_bg, (MAIN_WIDTH,MAIN_HEIGHT))
        elif player2.health <= 0:
            player1 = UI.select_character(UI.select_p1,1, settings)
            player2 = UI.select_character(UI.select_p2,2, settings)
            #current_bg = backgrounds[random.randint(0,2)]
            UI.gameover_menu(scale_factor_width, scale_factor_height, game_loop, settings, "Player 1")
            current_bg = backgrounds[random.randint(0,2)]
            current_bg = pygame.transform.scale(current_bg, (MAIN_WIDTH,MAIN_HEIGHT))
        if reset:
            player1 = UI.select_character(UI.select_p1,1, settings)
            player2 = UI.select_character(UI.select_p2,2, settings)
            current_bg = backgrounds[random.randint(0,2)]
            current_bg = pygame.transform.scale(current_bg, (MAIN_WIDTH,MAIN_HEIGHT))
            reset = not reset
        CLOCK.tick(FPS)
        pygame.display.flip()

    pygame.quit()

UI.main_menu(scale_factor_width, scale_factor_height, game_loop, settings)