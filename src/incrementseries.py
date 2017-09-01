





class IncrementSeries():
    
    def __init__(self, max):
        self._is_series = []
        for i in range(max):
            self._is_series.append(False)
            
        self._is_series[1] = True
        self._series = [1]
        
        last = 1
        increment = self.increment_start()
        increment_increase = self.increment_increase()
        next = 0
        for i in range(1, max):
            next = last + increment
            if next >= max:
                return
            self._series.append(next)
            self._is_series[next] = True
            last = next
            increment += self.increment_increase()
            
            
            
            
    def increment_start(self):
        return 2
    
    def increment_increase(self):
        return 1