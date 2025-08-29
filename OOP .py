class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def intro(self):
            print("My fruit is a", self.color, self.name,)
apple = Fruit('apple','red')
apple.intro()