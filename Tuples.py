#TUPLES.
#they are enclosed in regular brackets or quotes and unlike lists are immutable
def count_and_index(x, y):
    a = (x.count(y))
    print(y + " is repeated " + str(a) + " times!")
    print("AND")
    b = (x.index(y))
    print(y + " is first seen at index '" + str(b) + "'")

a = input("txt: ")
b = input("subject: ")
count_and_index(a, b)

#upon gaining further knowledge i made it a defined function. for ease of reading