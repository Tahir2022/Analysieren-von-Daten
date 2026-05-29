class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 3, 4]


    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


tom = Dog('Tom',30)
fred = Dog('Fred',10)
tom.change_age(2)
tom.add_weight(15)
tom.speak()
fred.speak()

print(tom.weight)
