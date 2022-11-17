class Stats_Bar:
    def __init__(self) -> None:
        self._hungry_stat = 250 # Default value for pet's hunger stat
        self._bored_stat = 250 # Default value for pet's boredom stat
    
    @property
    def hungry_stat(self) -> int:
        return self._hungry_stat

    @property
    def bored_stat(self) -> int:
        return self._bored_stat
        
    def update_hungry_stat(self, amount: int) -> None:
        '''
        Adds amount passed to hunger stat
        '''
        self._hungry_stat += amount

    def update_bored_stat(self, amount: int) -> None:
        '''
        Adds amount passed to boredom stat
        '''
        self._bored_stat += amount