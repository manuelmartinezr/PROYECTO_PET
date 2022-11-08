from pip import List
from Stats_Bar import Stats_Bar
from abc import ABC, abstractmethod
import random

class Pet(ABC):
    def __init__(self, name) -> None:
        self._name = name
        self._sex = random.choice(['male', 'female'])

    _desc : str
    _pet_idle : List
    _pet_eating : List
    _pet_playing: List
    
    @property
    def name(self):
        return self._name

    @property
    def sex(self):
        return self._sex

    @property
    def desc(self):
        return self._desc

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def pet_idle(self):
        ...

    @abstractmethod
    def pet_eats(self):
        ...

    @abstractmethod
    def pet_plays(self):
        ...

class Python(Pet):
    def __init__(self, name=None) -> None:
        super().__init__(name)

    desc = 'Python'
    _pet_idle = []
    _pet_eating = []
    _pet_playing = []

    def pet_idle(self):
        pass

    def pet_eats(self):
        pass
    
    def pet_plays(self):
        pass
