class Stats_Bar:
    def __init__(self) -> None:
        self._hungry_stat = 250
        self._bored_stat = 250
    
    @property
    def hungry_stat(self) -> int:
        return self._hungry_stat

    @property
    def bored_stat(self) -> int:
        return self._bored_stat
        
    def update_hungry_stat(self, amount: int) -> None:
        self._hungry_stat += amount

    def update_bored_stat(self, amount: int) -> None:
        self._bored_stat += amount