class Base:
    def __init__(self):
        self.a = "I have rights"
        self.__b = "and privileges"
        self.c = "to do whatever"
        self.d = "I please. "


class Derived(Base):
    def __init__(self):
        print(self.a)  # accessible
        print(self.b)
        print(self.c)
        print(self.d)


# Create an instance of the parent class

obj1 = Base()
print(obj1.a)
print(obj1.c)
print(obj1.d)
# print(obj1.b)
