secret_number = int(input("secret_number: "))
print('''








''')
Guess_Count = 1
Guess_limit = 3
while Guess_Count <= Guess_limit:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("Good Guess. You Won")
        break
    else:         #this else can be put under the while loop. thus automatically if guess_count > guess limit it runs the underlying program
        if Guess_Count == Guess_limit:
            print("Sorry You Failed")
    Guess_Count += 1
