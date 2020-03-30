class Person :
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi this is {self.name}")


person1 = Person(" james")
print(person1.name)
person1.talk()

person2 = Person('pillechan')
print(person2.name)
person2.talk()