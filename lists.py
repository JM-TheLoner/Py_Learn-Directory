brands = ["nike", "addidas", "puma", "fubu"] #lists use square brackets.
print(brands)
brands[1] = "adiddas" #this replaces the element on index 1 with the specified element
print(brands)
brands.append("jordans") #adds an element at the end of the list
print(brands)
brands.insert(3, "levi") #inserts specified character in specified index
print(brands)
print(brands[0:3:2]) #the first number is the start point, second is the end point, third number is the step
brands.remove("puma") #removes specified character
print(brands)
print(brands.pop())
print(brands.clear())
brands.sort() #sorts it alphanumerically
brands.reverse()  #in the name
brands2 = brands.copy()