class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bow... w... w...")
class Cat(Animal):
    def sound(self):
        print("Meow..... w.... w..")
for v in [Dog(),Cat()]:
    v.sound()

