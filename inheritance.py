class Mammal:
    def __init__(self, name):
        self.name = name
        print(f'Hi this is {name}')


    def walk(self):
        print('WALK')


class Dog(Mammal):


 class Cat(Mammal):
    pass


dog = Dog("ALsatian")
dog.walk()
