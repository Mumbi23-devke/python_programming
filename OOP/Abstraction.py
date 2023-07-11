class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("Meowwwww")


my_cat = Cat("Bootsy")
my_cat.make_sound()
