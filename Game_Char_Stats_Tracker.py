class GameCharacter:
    def __init__(self, name, mana, level, health):
        self._name = name
        self._mana = 50
        self._level = 1
        self._health = 100
        
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
        
    @health.getter
    def health(self):
        return self._health
        
    @health.setter
    def health(self, value):
        if value < 0 and value > 100:
            raise ValueError("Health must be between 0 and 100")
        self._health = value
    
    @property
    def mana(self):
        return self._mana
    
    @mana.getter
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, value):
        if value < 0 and value > 50:
            raise ValueError("Mana must be between 0 and 50")
        self._mana = value
    
    