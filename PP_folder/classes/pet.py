from abc import ABC
from .stats_bar import Stats_Bar
import random
import pygame

class Pet(ABC):
    def __init__(self, name: str) -> None:
        self._name = name # Pet's name
        self._sex = random.choice(['male', 'female']) # Pet's sex

    _desc : str # Type of pet
    _idle_animation : dict # Dict with pet's idle animation
    _eating_animation : dict # Dict with pet's eating animation
    _playing_animation: dict # Dict with pet's playing animation
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def sex(self) -> str:
        return self._sex

    @property
    def desc(self) -> str:
        return self._desc

    @property
    def idle_animation(self) -> dict:
        return self._idle_animation

    @property
    def eating_animation(self) -> dict:
        return self._eating_animation
    
    @property
    def playing_animation(self) -> dict:
        return self._playing_animation

    def eat(self, stats_bar: Stats_Bar) -> None:
        '''
        Update's the pet's hunger stat by a set amount
        '''
        stats_bar.update_hungry_stat(-200)

    def play(self, stats_bar: Stats_Bar) -> None:
        '''
        Update's the pet's boredom stat by a set amount
        '''
        stats_bar.update_bored_stat(-200)

class Python(Pet):
    def __init__(self, name = None) -> None:
        super().__init__(name)

    _desc = 'Python'
    _idle_animation = dict(pet_idle1 = pygame.image.load('PP_folder/assets/snake_idle1.png'),
                    pet_idle2 = pygame.image.load('PP_folder/assets/snake_idle2.png'))
    _eating_animation = dict(pet_eat1 = pygame.image.load('PP_folder/assets/snake_eats1.png'), 
                    pet_eat2 = pygame.image.load('PP_folder/assets/snake_eats2.png'),
                    pet_eat3 = pygame.image.load('PP_folder/assets/snake_eats3.png'), 
                    pet_eat4 = pygame.image.load('PP_folder/assets/snake_eats4.png'))
    _playing_animation = dict(pet_play1 = pygame.image.load('PP_folder/assets/snake_play1.png'), 
                    pet_play2 = pygame.image.load('PP_folder/assets/snake_play2.png'),
                    pet_play3 = pygame.image.load('PP_folder/assets/snake_plays3.png'), 
                    pet_play4 = pygame.image.load('PP_folder/assets/snake_plays4.png'), 
                    pet_play5 = pygame.image.load('PP_folder/assets/snake_eats4.png'))
