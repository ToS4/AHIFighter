import pygame
import json
import sys
import os
from ButtonController import Button, InputBox, CharacterBox

pygame.init()

# fixed Screen
WIDTH = 1000
HEIGHT = 600

# Fullscreen
SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
MAIN_WIDTH = SCREEN.get_width()
MAIN_HEIGHT = SCREEN.get_height()

# this is for scaling the font to fit the according screen
font_scaled = pygame.font.Font(None, int(35*MAIN_HEIGHT/HEIGHT))
# transparent color
transparent = pygame.Color(255,255,255,a=255)

# variable to reset the game
reset = False

def main_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    global reset
    reset = True
    # Creating the play button and settings its position
    play_button = Button(0,0,250,80,"black","PLAY","White",font_scaled
                        ,scale_width_factor, scale_height_factor, lambda: play_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT,
                                                                                    dest_gameloop, settings))
    play_button.rect.center = (MAIN_WIDTH/2 + 0*scale_width_factor, MAIN_HEIGHT/2-150*scale_height_factor)

    # Creating settings button and setting its position
    settings_button  = Button(0,0,300,80,"black","SETTINGS","white",font_scaled,
                            scale_width_factor, scale_height_factor, lambda: settings_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT,
                                dest_gameloop, settings))
    settings_button.rect.center = (MAIN_WIDTH/2+ 0*scale_width_factor, MAIN_HEIGHT/2)

    # Creating quit button and setting its position
    quit_button  = Button(0,0,250,80,"black","QUIT","white",font_scaled,
                            scale_width_factor, scale_height_factor, lambda: sys.exit())
    quit_button.rect.center = (MAIN_WIDTH/2+ 0*scale_width_factor, MAIN_HEIGHT/2 + 150*scale_height_factor)

    # MAIN MENU LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_button.handle_event(event)
                settings_button.handle_event(event)
                quit_button.handle_event(event)
            

        # always get the current mouse position
        mouse_position = pygame.mouse.get_pos()

        # these functions are responsible for the color change when hovering over the button
        play_button.hover_effect(mouse_position)
        settings_button.hover_effect(mouse_position)
        quit_button.hover_effect(mouse_position)

        # fill the screen white
        SCREEN.fill((255,255,255))

        #draws the buttons
        play_button.draw(SCREEN)
        settings_button.draw(SCREEN)
        quit_button.draw(SCREEN)

        pygame.display.update()

def pause_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    global reset
    reset = False
    # Creating the play button and settings its position
    continue_button = Button(0,0,250,80,"black","CONTINUE","White",font_scaled
                        ,scale_width_factor, scale_height_factor, lambda: dest_gameloop())
    continue_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2-75*scale_height_factor)

    # Creating quit button and setting its position
    back_button  = Button(0,0,250,80,"black","BACK TO MENU","white",font_scaled,
                            scale_width_factor, scale_height_factor, lambda: main_menu(scale_width_factor, scale_height_factor,
                                                                                        dest_gameloop, settings))
    back_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 75*scale_height_factor)

    # MAIN MENU LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                continue_button.handle_event(event)
                back_button.handle_event(event)
            

        # always get the current mouse position
        mouse_position = pygame.mouse.get_pos()

        # these functions are responsible for the color change when hovering over the button
        continue_button.hover_effect(mouse_position)
        back_button.hover_effect(mouse_position)

        # fill the screen white
        SCREEN.fill((255,255,255))

        #draws the buttons
        continue_button.draw(SCREEN)
        back_button.draw(SCREEN)

        pygame.display.update()

def settings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    # The responsible buttons for each players settings
    keybinds_p1_button = Button(0,0,300,80,"black","PLAYER 1","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: p1_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    keybinds_p1_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2-150*scale_height_factor))

    keybinds_p2_button = Button(0,0,300,80,"black","PLAYER 2","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: p2_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    keybinds_p2_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2))

    # a Button that returns you to the Main Menu
    back_button = Button(0,0,250,80,"black","BACK","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: main_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    back_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2+150*scale_height_factor))

    # This is to save the Keybinds every time you go back from p1- or p2-settings
    with open("settings.txt", "w") as file:
        text = json.dumps(settings)
        file.write(text)

    # Setting Menu loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                keybinds_p1_button.handle_event(event)
                keybinds_p2_button.handle_event(event)
                back_button.handle_event(event)

        mouse_position = pygame.mouse.get_pos()

        keybinds_p1_button.hover_effect(mouse_position)
        keybinds_p2_button.hover_effect(mouse_position)
        back_button.hover_effect(mouse_position)

        SCREEN.fill("white")

        keybinds_p1_button.draw(SCREEN)
        keybinds_p2_button.draw(SCREEN)
        back_button.draw(SCREEN)
        
        pygame.display.update()

def p1_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    # This is to create a "text", in reality it is a button with no functionality
    p1_text = Button(0,0,300,80,transparent,"PLAYER 1","black", font_scaled,scale_width_factor, scale_height_factor, None)
    p1_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 250*scale_height_factor)
    
    # a Button that returns you to the Main Menu
    back_button = Button(0,0,250,80,"black","BACK","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: settings_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT, dest_gameloop, settings))
    back_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2 + 250*scale_height_factor))

    # all input boxes for the keybinds
    left_kb_text = Button(0,0,300,80,transparent,"Move Left","black", font_scaled,scale_width_factor, scale_height_factor, None)
    left_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)
    left_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                       pygame.key.name(settings["player1"]["left"]))
    left_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)

    right_kb_text = Button(0,0,300,80,transparent,"Move Right","black", font_scaled,scale_width_factor, scale_height_factor, None)
    right_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2 - 100*scale_height_factor)
    right_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                        pygame.key.name(settings["player1"]["right"]))
    right_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2-100*scale_height_factor)

    jump_kb_text = Button(0,0,300,80,transparent,"Jump","black", font_scaled,scale_width_factor, scale_height_factor, None)
    jump_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)
    jump_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                       pygame.key.name(settings["player1"]["jump"]))
    jump_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)

    attack_kb_text = Button(0,0,300,80,transparent,"Attack","black", font_scaled,scale_width_factor, scale_height_factor, None)
    attack_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)
    attack_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                         pygame.key.name(settings["player1"]["attack"]))
    attack_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)

    block_kb_text = Button(0,0,300,80,transparent,"Block","black", font_scaled,scale_width_factor, scale_height_factor, None)
    block_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)
    block_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                         pygame.key.name(settings["player1"]["block"]))
    block_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)

    ability_kb_text = Button(0,0,300,80,transparent,"Ability","black", font_scaled,scale_width_factor, scale_height_factor, None)
    ability_kb_text.rect.center = (MAIN_WIDTH/2+ 120*scale_width_factor, MAIN_HEIGHT/2-175*scale_height_factor)
    ability_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                         pygame.key.name(settings["player1"]["ability"]))
    ability_kb.rect.center = (MAIN_WIDTH/2+240*scale_width_factor, MAIN_HEIGHT/2-175*scale_height_factor)

    # list that contains all the input boxes
    inputs = [left_kb, right_kb, jump_kb, attack_kb, block_kb, ability_kb]

    # list that contains the texts of these boxes
    texts = [left_kb_text, right_kb_text, attack_kb_text, jump_kb_text, block_kb_text, ability_kb_text]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_button.handle_event(event)
            
            settings["player1"]["left"] = pygame.key.key_code(left_kb.handle_event(event))
            settings["player1"]["right"] = pygame.key.key_code(right_kb.handle_event(event))
            settings["player1"]["jump"] = pygame.key.key_code(jump_kb.handle_event(event))
            settings["player1"]["attack"] = pygame.key.key_code(attack_kb.handle_event(event))
            settings["player1"]["block"] = pygame.key.key_code(block_kb.handle_event(event))
            settings["player1"]["ability"] = pygame.key.key_code(ability_kb.handle_event(event))
        
        mouse_position = pygame.mouse.get_pos()

        # p1_button should not be added here, since its not displayed as a button
        back_button.hover_effect(mouse_position)
        
        SCREEN.fill((255,255,255))

        p1_text.draw(SCREEN)
        back_button.draw(SCREEN)

        for i in texts:
            i.draw(SCREEN)
        for i in inputs:
            i.draw(SCREEN)

        pygame.display.update()

def p2_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    # This is to create a "text", in reality it is a button with no functionality
    p2_text = Button(0,0,300,80,transparent,"PLAYER 2","black", font_scaled,scale_width_factor, scale_height_factor, None)
    p2_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 250*scale_height_factor)
    
    # a Button that returns you to the Main Menu
    back_button = Button(0,0,250,80,"black","BACK","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: settings_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT, dest_gameloop, settings))
    back_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2 + 250*scale_height_factor))

    # all input boxes for the keybinds
    left_kb_text = Button(0,0,300,80,transparent,"Move Left","black", font_scaled,scale_width_factor, scale_height_factor, None)
    left_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)
    left_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                       pygame.key.name(settings["player2"]["left"]))
    left_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)

    right_kb_text = Button(0,0,300,80,transparent,"Move Right","black", font_scaled,scale_width_factor, scale_height_factor, None)
    right_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2 - 100*scale_height_factor)
    right_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                        pygame.key.name(settings["player2"]["right"]))
    right_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2-100*scale_height_factor)

    jump_kb_text = Button(0,0,300,80,transparent,"Jump","black", font_scaled,scale_width_factor, scale_height_factor, None)
    jump_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)
    jump_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                       pygame.key.name(settings["player2"]["jump"]))
    jump_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)

    attack_kb_text = Button(0,0,300,80,transparent,"Attack","black", font_scaled,scale_width_factor, scale_height_factor, None)
    attack_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)
    attack_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                         pygame.key.name(settings["player2"]["attack"]))
    attack_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)

    block_kb_text = Button(0,0,300,80,transparent,"Block","black", font_scaled,scale_width_factor, scale_height_factor, None)
    block_kb_text.rect.center = (MAIN_WIDTH/2-240*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)
    block_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                         pygame.key.name(settings["player2"]["block"]))
    block_kb.rect.center = (MAIN_WIDTH/2+0*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)

    ability_kb_text = Button(0,0,300,80,transparent,"Ability","black", font_scaled,scale_width_factor, scale_height_factor, None)
    ability_kb_text.rect.center = (MAIN_WIDTH/2+ 120*scale_width_factor, MAIN_HEIGHT/2-175*scale_height_factor)
    ability_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings, "player2",
                         pygame.key.name(settings["player2"]["ability"]))
    ability_kb.rect.center = (MAIN_WIDTH/2+240*scale_width_factor, MAIN_HEIGHT/2-175*scale_height_factor)

    # list that contains all the input boxes
    inputs = [left_kb, right_kb, jump_kb, attack_kb, block_kb, ability_kb]

    # list that contains the texts of these boxes
    texts = [left_kb_text, right_kb_text, attack_kb_text, jump_kb_text, block_kb_text, ability_kb_text]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_button.handle_event(event)
            
            settings["player2"]["left"] = pygame.key.key_code(left_kb.handle_event(event))
            settings["player2"]["right"] = pygame.key.key_code(right_kb.handle_event(event))
            settings["player2"]["jump"] = pygame.key.key_code(jump_kb.handle_event(event))
            settings["player2"]["attack"] = pygame.key.key_code(attack_kb.handle_event(event))
            settings["player2"]["block"] = pygame.key.key_code(block_kb.handle_event(event))
            settings["player2"]["ability"] = pygame.key.key_code(ability_kb.handle_event(event))
        
        mouse_position = pygame.mouse.get_pos()

        # p1_button should not be added here, since its not displayed as a button
        back_button.hover_effect(mouse_position)
        
        SCREEN.fill((255,255,255))

        p2_text.draw(SCREEN)
        back_button.draw(SCREEN)

        for i in texts:
            i.draw(SCREEN)
        for i in inputs:
            i.draw(SCREEN)

        pygame.display.update()

def play_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    
    player = 1

    start_button = Button(0,0,250,80,"black","START","white",font_scaled,scale_width_factor, scale_height_factor,dest_gameloop)
    start_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 200 * scale_height_factor)

    # This will be the box for the knight selection
    knight_box = CharacterBox(0,0,100,100,"white",scale_width_factor, scale_height_factor, "Knight")
    knight_box.rect.center = (MAIN_WIDTH/2-120*scale_width_factor, MAIN_HEIGHT/2 - 80 * scale_height_factor)
    knight_img = pygame.image.load(os.path.join("src/assets/imgs/Knight/Icon.png")).convert_alpha()
    knight_img = pygame.transform.scale(knight_img, (99*scale_width_factor, 99*scale_height_factor))
    knight_select = False

    # This will be the box for the mage selection
    wizard_box = CharacterBox(0,0,100,100,"white",scale_width_factor, scale_height_factor, "Wizard")
    wizard_box.rect.center = (MAIN_WIDTH/2-0*scale_width_factor, MAIN_HEIGHT/2 - 80 * scale_height_factor)
    wizard_img = pygame.image.load(os.path.join("src/assets/imgs/LightningMage/Icon.png")).convert_alpha()
    wizard_img = pygame.transform.scale(wizard_img, (99*scale_width_factor, 99*scale_height_factor))
    wizard_select = False

    # This will be the box for Nathan selection
    nathan_box = CharacterBox(0,0,100,100,"white",scale_width_factor, scale_height_factor, "??")
    nathan_box.rect.center = (MAIN_WIDTH/2+120*scale_width_factor, MAIN_HEIGHT/2 - 80 * scale_height_factor)
    nathan_img = pygame.image.load(os.path.join("src/assets/imgs/BuckBorris/Icon.png")).convert_alpha()
    nathan_img = pygame.transform.scale(nathan_img, (99*scale_width_factor, 99*scale_height_factor))
    nathan_select = False

    char = ""
    text = Button(0,0,300,80,(255,255,255,0),char,"black", font_scaled,scale_width_factor, scale_height_factor, None)
    text.rect.width = 10
    text.rect.height = 10
    text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 40*scale_height_factor)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_button.handle_event(event)
                if player == 1:
                    if knight_box.rect.collidepoint(mouse_pos):
                        knight_box.select()
                        player += 1
                        knight_select = True
                    elif wizard_box.rect.collidepoint(mouse_pos):
                        wizard_box.select()
                        player += 1
                        wizard_select = True
                    elif nathan_box.rect.collidepoint(mouse_pos):
                        nathan_box.select()
                        player += 1
                        nathan_select = True
                elif player == 2:
                    if knight_box.rect.collidepoint(mouse_pos) and not knight_select:
                        knight_box.select()
                        player = "2"
                    elif wizard_box.rect.collidepoint(mouse_pos) and not wizard_select:
                        wizard_box.select()
                        player = "2"
                    elif nathan_box.rect.collidepoint(mouse_pos) and not nathan_select:
                        nathan_box.select()
                        player = "2"
                    

        if knight_box.rect.collidepoint(mouse_pos):
            char = knight_box.char
        elif wizard_box.rect.collidepoint(mouse_pos):
            char = wizard_box.char
        elif nathan_box.rect.collidepoint(mouse_pos):
            char = nathan_box.char
        else:
            char = ""
        
        text = Button(0,0,300,80,(255,255,255,0),char,"black", font_scaled,scale_width_factor, scale_height_factor, None)
        text.rect.width = 10
        text.rect.height = 10
        text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 30*scale_height_factor)

        selecting_text = Button(0,0,400,150,transparent, f"Player {player} is selecting...","black",font_scaled,
                            scale_width_factor,scale_height_factor)
        selecting_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 220 * scale_height_factor)

    
        SCREEN.fill((255,255,255))

        start_button.hover_effect(mouse_pos)

        selecting_text.draw(SCREEN)
        start_button.draw(SCREEN)
        knight_box.draw(SCREEN)
        wizard_box.draw(SCREEN)
        nathan_box.draw(SCREEN)
        text.draw(SCREEN)

        # this will blit the images into the boxes
        SCREEN.blit(knight_img, knight_box)
        SCREEN.blit(wizard_img, wizard_box)
        SCREEN.blit(nathan_img, nathan_box)
        
        pygame.display.update()

def gameover_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings, player):

    who_won_text = Button(0,0,250,80,transparent,f"{player} won!","black", font_scaled,scale_width_factor, scale_height_factor, None)
    who_won_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 250*scale_height_factor)

    play_button = Button(0,0,250,80,"black","PLAY AGAIN","White",font_scaled
                        ,scale_width_factor, scale_height_factor, lambda: dest_gameloop())
    play_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2- 50*scale_height_factor)

    back_button = Button(0,0,300,80,"black","BACK TO LOBBY","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: main_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    back_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 150*scale_height_factor)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_button.handle_event(event)
                back_button.handle_event(event)

        mouse_position = pygame.mouse.get_pos()

        play_button.hover_effect(mouse_position)
        back_button.hover_effect(mouse_position)

        SCREEN.fill((255,255,255))
        
        play_button.draw(SCREEN)
        back_button.draw(SCREEN)
        who_won_text.draw(SCREEN)

        pygame.display.update()

#asdf
if __name__ == "__main__":
    play_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT, None, None, "Player 1")
