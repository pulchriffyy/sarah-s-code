class rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def rectangle_area(self):
        return self.length*self.width 
newrectangle = rectangle(12, 10)
print("Dimension of rectangle - length : %d width : %d"% (newrectangle.length, newrectangle.width))
print("Area of rectangle:", newrectangle.rectangle_area())