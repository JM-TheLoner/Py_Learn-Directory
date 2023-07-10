try:
    name = input("Name should be more than 3 letters: ")
    if len(name) < 3:
        raise ValueError
except ValueError:
    print("Invalid name")
    print("Name should be more than 3 letters")
    name = ("Invalid. \nPlease try again")
else:
    print("Accoount Created")

finally:
    print("Account name is " + name)
