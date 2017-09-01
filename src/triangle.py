
from incrementseries import IncrementSeries


class Triangle(IncrementSeries):
    
    
    
    def increment_start(self):
        return 2
    
    def increment_increase(self):
        return 1
    
    
    def __init__(self, max):
        IncrementSeries.__init__(self, max)
        self.is_triangle = self._is_series
        self.triangle_numbers = self._series






if __name__ == "__main__":
    nums1 = Triangle(350).triangle_numbers
    print(str(nums1))
    
    nums2 = Triangle(330).triangle_numbers
    print(str(nums2))