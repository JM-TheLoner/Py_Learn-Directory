import random 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]    #this works with the .sampke method


for i in range (3):                #fyi... from this point it is shown as .method(argument, argument)
    print(random.random())               #.random() choses a random number between 0 and 1
    print(random.randint(10, 20))        #.randint(int, int)  choses a random number between two integers. the integers icluded as possible choices
    print(random.choice(numbers))        #.choice(list) choses a random object from "list"
    print(random.sample(numbers, 4))        #.sample(list, number) takes "number" random objects from "list" 

    print("===============================")
