def decor(func):
    print("===============================")
    func()
    print("===============================")

#decorator can be:

@decor
def greet():
    input()

greet

#or

def greet():
    input()

decor(greet)

#or

def greet():
    input()

greet = decor(greet)