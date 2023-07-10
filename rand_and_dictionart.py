import random

a = "atmospheric pressure"
b = "Bank Of Fuckery"
c = "Nameless Bank"
d = "This is a completely random message"
e = "I AM HIM"

statements = {
    a:"1",
    b:"2",
    c:"3",
    d:"4",
    e:"5"
}


choices = random.randint(1,5)
choice = str(choices)

for i in statements:
    if statements[i] == choice:
        dec=i
        break

print(dec)   # type: ignore