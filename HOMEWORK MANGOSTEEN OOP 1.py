class FRUIT:
    def __init__(self,name,color):
        self.name = name
        self.color = color
Mangosteen = FRUIT('mangosteen', 'dark purple')
        # object declaration outside
print('its a', Mangosteen.name)