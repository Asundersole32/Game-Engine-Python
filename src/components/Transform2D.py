import Vector2D


origin = Vector2D(0.0, 0.0)
x = Vector2D(1.0, 0.0)
y = Vector2D(0.0, 1.0)

class Transform2D():
    def __init__(self, origin:Vector2D = origin, x:Vector2D = x, y:Vector2D = y):
        self.origin = origin
        self.x = x
        self.y = y