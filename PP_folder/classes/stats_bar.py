class Stats_Bar:
    def __init__(self) -> None:
        self._hungry_stat = 250
        self._bored_stat = 250
    
    def update_hungry_stat(self, amount: int) -> None:
        self._hungry_stat += amount

    def update_bored_stat(self, amount: int) -> None:
        self._bored_stat += amount