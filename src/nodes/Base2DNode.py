import BaseNode
from components.Vector2D import Vector2D

global_position = Vector2D()
global_scale = Vector2D(1.0, 1.0)
position = Vector2D()
scale = Vector2D(1.0, 1.0)

class Base2DNode(BaseNode):
    def __int__(self, 
                global_position: Vector2D = global_position, 
                global_rotation: float = 0.0, 
                global_rotation_degrees: float = 0.0, 
                global_scale: Vector2D = global_scale, 
                global_skew: float = 0.0,
                position: Vector2D = position,
                rotation: float = 0.0,
                rotation_degrees: float = 0.0,
                scale: Vector2D = scale,
                skew: float = 0.0):
        
        self.global_position = global_position
        self.global_rotation = global_rotation
        self.global_rotation_degrees = global_rotation_degrees
        self.global_scale = global_scale
        self.global_skew = global_skew
        self.position = position
        self.rotation = rotation
        self.rotation_degrees = rotation_degrees
        self.scale = scale
        self.skew = skew

