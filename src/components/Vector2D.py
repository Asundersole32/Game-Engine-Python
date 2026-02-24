class Vector2D():
    def __init__(self, x:float=0.0, y:float=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def set_x(self, x:float=0.0):
        self.x = x
        return self
    
    def get_y(self):
        return self.y
    
    def set_y(self, y:float=0.0):
        self.y = y
        return y
    
    def get_tuple(self):
        return (self.x, self.y)
    
    def set_coord(self, x:float=0.0, y:float=0.0):
        self.x = x
        self.y = y
        return self