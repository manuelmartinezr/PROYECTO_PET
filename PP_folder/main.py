import pygame
from display import *
from sys import exit
from user import User
from button import Button
from pet import Pet, Python
from stats_bar import Stats_Bar

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Posada-Plays Co')
clock = pygame.time.Clock()
font = pygame.font.Font('/Users/manuel/Documents/font/Pixeltype.ttf', 50)

BG = pygame.Surface((WIDTH, HEIGHT))
BG.fill(GREEN)
startmsg_surf = font.render('Welcome to PyPet!', False, 'Black')
startmsg_rect = startmsg_surf.get_rect(center = (250, 100))

startbtn_surf = font.render('Start', False, 'Black')
startbtn_rect = startbtn_surf.get_rect(center = (250, 300))
idle_index = 0

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font('/Users/manuel/Documents/font/Pixeltype.ttf', size)

def get_pet(pet_classes: list[Pet], user_input: str):
    for pet_class in pet_classes:
            if pet_class.desc.lower() == user_input.lower():
                new_pet = pet_class
                return new_pet

def idle_animation(pet_idle):
    global pet_surf, idle_index
    idle_index += 0.1
    if idle_index >= len(pet_idle) : idle_index = 0


def start():

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))
        
        PLAY_TEXT = get_font(45).render('Welcome to PyPet!', False, 'Black')
        PLAY_RECT = PLAY_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_START = Button(image=None, pos=(250, 300), 
                            text_input='Start', font= get_font(45), base_color='Black', hovering_color='Gray' )

        PLAY_START.changeColor(PLAY_MOUSE_POS)
        PLAY_START.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_START.checkForInput(PLAY_MOUSE_POS):
                    #here is where u call function that will display screen
                    #for user to create the pet
                    #put the imgs and fonts in a local folder 
                    options()

        pygame.display.update()
        clock.tick(60)

def options():

    list_of_pets = 'Python'

    pet_classes = [Python()]

    user_text = ''

    input_rect = pygame.Rect(200, 250, 150, 32)

    while True:
        SCREEN.blit(BG, (0,0))

        OPT_TEXT = get_font(45).render('List of available pets: ' + list_of_pets, False, 'Black')
        OPT_RECT = OPT_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(OPT_TEXT, OPT_RECT)
        OPT_TEXT2 = get_font(45).render('Enter your chosen pet:', False, 'Black')
        OPT_RECT2 = OPT_TEXT2.get_rect(center=(250, 200))
        SCREEN.blit(OPT_TEXT2, OPT_RECT2)

        pygame.draw.rect(SCREEN, 'Black', input_rect, 2)
        user_text_surf = get_font(45).render(user_text, False, 'Black' )
        SCREEN.blit(user_text_surf, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, user_text_surf.get_width() + 10)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if user_text in list_of_pets:
                        new_pet = get_pet(pet_classes, user_text)
                        #call function to display screen with the pet
                        user_settings(new_pet)
                else:
                    user_text += event.unicode

        pygame.display.update()
        clock.tick(60)

def user_settings(new_pet):
    user_text = ''

    input_rect = pygame.Rect(200, 250, 150, 32)

    while True:
        OPT_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))
        STG_TEXT = get_font(45).render('Enter your name:', False, 'Black')
        STG_RECT = STG_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(STG_TEXT, STG_RECT)
        
        pygame.draw.rect(SCREEN, 'Black', input_rect, 2)
        user_text_surf = get_font(45).render(user_text, False, 'Black' )
        SCREEN.blit(user_text_surf, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, user_text_surf.get_width() + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    user = User(user_text)
                    pet_settings(user, new_pet)
                else:
                    user_text += event.unicode

        pygame.display.update()
        clock.tick(60)

def pet_settings(user, new_pet):
    user_text = ''

    input_rect = pygame.Rect(200, 250, 150, 32)

    while True:
        SCREEN.blit(BG, (0,0))
        STG_TEXT = get_font(45).render("Enter your pet's name:", False, 'Black')
        STG_RECT = STG_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(STG_TEXT, STG_RECT)
        
        pygame.draw.rect(SCREEN, 'Black', input_rect, 2)
        user_text_surf = get_font(45).render(user_text, False, 'Black' )
        SCREEN.blit(user_text_surf, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, user_text_surf.get_width() + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    user.Pet = new_pet
                    user.Pet.name = user_text
                    game(user)
                else:
                    user_text += event.unicode

        pygame.display.update()
        clock.tick(60)

def game(user):
    pet_idle = [user.Pet._pet_idle['pet_idle1'], user.Pet._pet_idle['pet_idle2']]
    pet_surf = pet_idle[int(idle_index)].convert_alpha()
    stats = Stats_Bar()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))
        
        pet_surf = pet_idle[int(idle_index)].convert_alpha()
        pet_rect = pet_surf.get_rect(center = (250, 300))
        
        PLAY_BTN = Button(image=pygame.image.load('/Users/manuel/Documents/toyicon1.png'), pos=(400, 50), 
                            text_input='', font= get_font(45), base_color='Black', hovering_color='Gray' )
        PLAY_BTN.update(SCREEN)

        FOOD_BTN = Button(image=pygame.image.load('/Users/manuel/Documents/foodicon1.png'), pos=(400, 150), 
                            text_input='', font= get_font(45), base_color='Black', hovering_color='Gray' )
        FOOD_BTN.update(SCREEN)

        idle_animation(pet_idle)
        SCREEN.blit(pet_surf, pet_rect)
        stats.update_bored_stat(0.01)
        stats.update_hungry_stat(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BTN.checkForInput(PLAY_MOUSE_POS) and stats._bored_stat>200:
                    stats.update_bored_stat(-200)
                if FOOD_BTN.checkForInput(PLAY_MOUSE_POS) and stats._hungry_stat>200:
                    stats.update_hungry_stat(-200)
        print(stats._hungry_stat)

        if stats._hungry_stat > 253:
            game_over()

        pygame.display.update()
        clock.tick(20)

def game_over():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))
        
        PLAY_TEXT = get_font(45).render('Tu mascota se fue a un mejor lugar', False, 'Black')
        PLAY_RECT = PLAY_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_START = Button(image=None, pos=(250, 300), 
                            text_input='Back to Start', font= get_font(45), base_color='Black', hovering_color='Gray' )

        PLAY_START.changeColor(PLAY_MOUSE_POS)
        PLAY_START.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_START.checkForInput(PLAY_MOUSE_POS):
                    
                    start()

        pygame.display.update()
        clock.tick(60)

start()