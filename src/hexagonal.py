

from incrementseries import IncrementSeries




class Hexagonal(IncrementSeries):
    
    def __init__(self, max):
        IncrementSeries.__init__(self, max)
        self.is_hexagonal = self._is_series
        self.hexagonal_numbers = self._series
        
    def increment_start(self):
        return 5
    
    
    def increment_increase(self):
        return 4