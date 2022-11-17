import pygame
from display import *
from sys import exit
from classes.user import User
from classes.button import Button
from classes.pet import Pet, Python
from classes.stats_bar import Stats_Bar

# Setting the display
pygame.init()
pygame.display.set_caption('Posada-Plays Co')
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting the background
BG = pygame.Surface((WIDTH, HEIGHT))
BG.fill(GREEN)

idle_index = 0 # For idle animation

def get_font(size): # Returns Press-Start-2P font in the desired size
    return pygame.font.Font('PP_folder/assets/font/Pixeltype.ttf', size)

def get_pet(pet_classes: list[Pet], user_input: str) -> Pet:
    for pet_class in pet_classes:
            if pet_class.desc.lower() == user_input.lower():
                new_pet = pet_class
                return new_pet

def do_idle_animation(idle_list: list) -> None:
    global pet_surf, idle_index
    idle_index += 0.1
    if idle_index >= len(idle_list) : idle_index = 0

def show_start() -> None:
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
                    show_opts()

        pygame.display.update()
        clock.tick(60)

def show_opts() -> None:

    pets_available = 'Python' #Open for extension
    
    pet_classes = [Python()]

    user_input = ''

    input_rect = pygame.Rect(200, 250, 150, 32)

    while True:

        SCREEN.blit(BG, (0,0))

        OPT_TEXT = get_font(45).render(f'List of available pets: {pets_available}', False, 'Black')
        OPT_RECT = OPT_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(OPT_TEXT, OPT_RECT)
        OPT_TEXT2 = get_font(45).render('Enter your chosen pet:', False, 'Black')
        OPT_RECT2 = OPT_TEXT2.get_rect(center=(250, 200))
        SCREEN.blit(OPT_TEXT2, OPT_RECT2)

        pygame.draw.rect(SCREEN, 'Black', input_rect, 2)
        user_input_surf = get_font(45).render(user_input, False, 'Black' )
        SCREEN.blit(user_input_surf, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, user_input_surf.get_width() + 10)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    user_input = user_input.capitalize()
                    if user_input in pets_available:
                        new_pet = get_pet(pet_classes, user_input)
                        show_user_stgs(new_pet)
                else:
                    user_input += event.unicode

        pygame.display.update()
        clock.tick(60)

def show_user_stgs(new_pet: Pet) -> None:
    user_input = ''

    input_rect = pygame.Rect(200, 250, 150, 32)

    while True:
        SCREEN.blit(BG, (0,0))
        STG_TEXT = get_font(45).render('Enter your name:', False, 'Black')
        STG_RECT = STG_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(STG_TEXT, STG_RECT)
        
        pygame.draw.rect(SCREEN, 'Black', input_rect, 2)
        user_input_surf = get_font(45).render(user_input, False, 'Black' )
        SCREEN.blit(user_input_surf, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, user_input_surf.get_width() + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    user = User(user_input)
                    show_pet_stgs(user, new_pet)
                else:
                    user_input += event.unicode

        pygame.display.update()
        clock.tick(60)

def show_pet_stgs(user: User, new_pet: Pet) -> None:
    user_input = ''

    input_rect = pygame.Rect(200, 250, 150, 32)

    while True:
        SCREEN.blit(BG, (0,0))
        STG_TEXT = get_font(45).render("Enter your pet's name:", False, 'Black')
        STG_RECT = STG_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(STG_TEXT, STG_RECT)
        
        pygame.draw.rect(SCREEN, 'Black', input_rect, 2)
        user_input_surf = get_font(45).render(user_input, False, 'Black' )
        SCREEN.blit(user_input_surf, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, user_input_surf.get_width() + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    user.Pet = new_pet
                    user.Pet.name = user_input
                    show_game(user)
                else:
                    user_input += event.unicode

        pygame.display.update()
        clock.tick(60)

def show_game(user: User) -> None:
    idle_list = [animation for animation in user.Pet.idle_animation.values()]
    
    stats = Stats_Bar()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))
        
        pet_surf = idle_list[int(idle_index)].convert_alpha()
        pet_rect = pet_surf.get_rect(center = (250, 300))
        
        PLAY_BTN = Button(image=pygame.image.load('PP_folder/assets/icons/toyicon1.png'), pos=(400, 50), 
                            text_input='', font= get_font(45), base_color='Black', hovering_color='Gray' )
        PLAY_BTN.update(SCREEN)
        FOOD_BTN = Button(image=pygame.image.load('PP_folder/assets/icons/foodicon1.png'), pos=(400, 150), 
                            text_input='', font= get_font(45), base_color='Black', hovering_color='Gray' )
        FOOD_BTN.update(SCREEN)

        stats.update_bored_stat(0.01)
        stats.update_hungry_stat(0.01)

        HNG_TXT = get_font(45).render(f'Hunger : {int(stats.hungry_stat)} / 5000', False, 'Black')
        HNG_RECT = HNG_TXT.get_rect(topleft=(50, 50))
        SCREEN.blit(HNG_TXT, HNG_RECT)

        BRD_TXT = get_font(45).render(f'Boredom: {int(stats.bored_stat)}/ 5000', False, 'Black')
        BRD_RECT = BRD_TXT.get_rect(topleft=(50, 80))
        SCREEN.blit(BRD_TXT, BRD_RECT) 

        SOME_TXT = get_font(45).render(f'{user.Pet.name} is looking at {user.Name}...', False, 'Black')
        SOME_RECT = SOME_TXT.get_rect(topleft=(50, 200))
        SCREEN.blit(SOME_TXT, SOME_RECT) 

        do_idle_animation(idle_list)
        SCREEN.blit(pet_surf, pet_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BTN.checkForInput(PLAY_MOUSE_POS) and stats.hungry_stat >200:
                    user.Pet.eat(stats)
                if FOOD_BTN.checkForInput(PLAY_MOUSE_POS) and stats.bored_stat > 200:
                    user.Pet.play(stats)

        if stats.hungry_stat > 253 or stats.bored_stat > 253:
            show_end(user)

        pygame.display.update()
        clock.tick(20)

def show_end(user) -> None:
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))
        
        PLAY_TEXT = get_font(45).render(f'{user.Pet.name} se fue a un mejor lugar', False, 'Black')
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
                    show_start()

        pygame.display.update()
        clock.tick(60)

show_start()