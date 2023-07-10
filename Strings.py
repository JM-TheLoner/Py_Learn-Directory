first = "Jay"
last = "zee"

msg = f'{first} [{last}] is a coder' #this is a formatted string, thus the f in front of the quotation mark
print(msg)                           #its a method of concatenation

print(msg.upper())    #method to make string uppercase but doesnt change it
print(msg.lower())
print(msg.title())
print(msg.find("is"))
print(msg.replace("is", "was"))
"Jay" in msg
print(msg)


print(type(168.3))