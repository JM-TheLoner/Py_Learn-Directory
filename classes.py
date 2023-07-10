class athlete:                                             #this is a superclass (a class that sets the stage for other classes)
    def __init__(self, name, age, height, position):       #this is used when different classes have similar attributes
        self.name = name                                   #format is to be strictly followed
        self.position = position                           #look below for the differences
        self.age = age                                     #this cn function as a class on its own
        self.height = height
    

    def gender(self):
        print("male")


class football(athlete):                  #this is an example of a subclass that INHERITS from the superlass
    def score(self):                      #showing its unique nature.
        print("GOAL!!!!!")                #if no unique nature is found, more definitions can be added in bracket after init

                                          # just to be clear, these natures can be defined even if there is nu subclass
class basketball(athlete):
    def score(self):
        print("SWOOSH!!!!!")


class baseball(athlete):
    def score(self):
        print("HOME RUN!!!!")

    
ronaldo = football("ronaldo", 34, 176, "forward")
ronaldo.score()
print(ronaldo.age)
ronaldo.gender()


kobe = basketball("kobe bryant", 37, 186, "forward")
kobe.score()
print(kobe.age)


class a:
    def spam(self):
        print(1)

class b(a):
    def spam(self):
        print(2)
        super().spam()       #super here brings out both the spam outputs.
                             #without it, the 2 overwrites the one and comes out alone

b().spam()


#there are things known as magic methods. they are have 2 underscores infront and behind them
# add(+) , sub(-), mul(*), truediv(/), floordiv(//), mod(%), pow(**), and(&), xor(^), or(~)
#the ~ isnt that its the straight line im supposed to get when i press the key on the keyboard
#in the instance "a + b" if a isnt implemented for the stated function, it goes "b + a" but here its not add but radd.
#there are r versions for every one stated above
#lt(<), le(<=), eq(=), ne(!=), gt(>), ge(>=)
#there are many other methods