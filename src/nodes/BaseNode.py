

class BaseNode():
    def __init__(self, components = None):
        self.components = components

    def get_components(self):
        return self.components
    
    def set_components(self, components = None):
        self.components = components
        return self
    