word = input()
vowels = ["a", "e", "i", "o", "u"]
a = {i for i in word if i in vowels} #this means a = i... but only the ones that fulfil the required xistics
#this checks every element in the given input and checks it against the vowels list.
#only elements NOT IN vowels are allowed and then assigned to "a"
#the square brackets to make output a list
# the brackets can be {set} or [list] or (tuple)
print(a)