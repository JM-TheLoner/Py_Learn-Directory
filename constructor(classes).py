#constructor is a function that gets called at the point of calling an obect {Class}

class Point():
    def __init__(self, x, y):         #this is a constructor
        self.x = x
        self.y = y


point1 = Point(10, 20)     #this gives the same result as assigning point1.x and point1.y as seen above
print(point1.x)

#tests

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hello, my name is {self.name}")


first = Person("John Doe")
print(first.name)
first.talk()