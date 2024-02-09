class health():
    def __init__(self, points):
        self.points = points
    
    def get_health(self):
        return self.points
    
    def set_health(self, x):
        self.points = x
