class Shape:
    def __init__(self,_width,_height):
        self.witdh=_width
        self.Height=_height
        
        

class ColoredShape(Shape):
    def __init__(self,_witdh,_height,_color):
        super().__init__()
        self.Color=_color
        
        
obj=ColoredShape(300,200,"red")