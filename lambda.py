from __future__ import print_function

def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2*x*x, 5))
a = (lambda x,y: (x/y)*100) (3, 4) #lambda is used for simple one line functions.
print(a)


#there is more than one format for lambda. above are 2 shown