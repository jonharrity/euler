



from incrementseries import IncrementSeries


class Pentagonal(IncrementSeries):
    
    
    def __init__(self, max):
        IncrementSeries.__init__(self, max)
        self.is_pentagonal = self._is_series
        self.pentagonal_numbers = self._series
        
    def increment_start(self):
        return 4
    
    def increment_increase(self):
        return 3