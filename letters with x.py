ranges = [5, 2, 5, 2, 2]
for x_count in ranges:
    output = ""    #empty string
    for count in range(x_count):   #this gives a number of values as you know
        output += "x"    #the number gotten above will be the number of "X" added to a blank output
    print(output)        

print("=" *  8)   #above and below are same code

ranges = [5, 2, 5, 2, 2]
for x_count in ranges: 
    print(x_count * "x")