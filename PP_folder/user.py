from pet import Pet

class User:
    def __init__(self, name: str) -> None:
        self._name = name
        self._pet : Pet

    @property 
    def Name(self) -> str:
        return self._name

    @property
    def Pet(self) -> Pet:
        return self._pet

    @Pet.setter
    def Pet(self, Pet: Pet):
        self._pet = Pet