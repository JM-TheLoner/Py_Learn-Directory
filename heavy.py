text = input() #to take the text
dict = {} #the brackets used make the dict a set and eliminates repetition
for x in text: #to check every character one by one
    dict[x] = text.count(x) #assigning to each character in the set its count. x = 0, 1, 2, 3,... 
print(dict)

#above code takes an input and shows how many times each character was used