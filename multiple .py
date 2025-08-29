class Birds:
    # class atribute
    species = "Chickadee"
    # instance atribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # initiate the class
bob = Birds("bob", 1000)
bobbita = Birds("bobbita", 999)
print("bob is a {}".format(bob.species))
print("bobbita is a {}".format(bobbita.species))
print("{} is {} years old!".format(bob.name, bob.age))
print("{} is {} years old!".format(bobbita.name, bobbita.age))