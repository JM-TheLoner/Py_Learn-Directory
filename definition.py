def even(x): #def lets you define new functions
    if x % 2 == 0: 
        return ("even")
    else:
        return ("odd")


print(even(28))
print(even(57))   

#as you noticed there has to be 2 blank lines between the end of the definition and the next line of code

def percentage(x,y):
    ANS = str((x / y) * 100)
    print(str(x) + " is " + ANS + " percent of " + str(y))


a = float(input("numerator: "))
b = float(input("denominator: "))
print(percentage(a,b))