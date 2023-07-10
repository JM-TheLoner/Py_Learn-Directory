state = ""
new_state_1 = False
new_state_2 = True #you could replace this in the with "not new_state_1" this is primitive
while True:         #the above is true not false cuz the car starts stopped
    state = input("> ").lower()   #this is in here and not before the loop else after one input the loop continues on that one input infinitely
    if state == "start":
        if new_state_1 == False:
            print("Car started...Ready to go")
            new_state_1 = True
        else:
            print("Car already Started")

    
    elif state == "stop":
        if new_state_2 == False:
            print("Car Stopped")
            new_state_2 = True
        else:
            print("Car already Stopped")
        
    elif state == "help":
        print('''start - to start the car
stop - to stop the car
quit - quit game''')

    elif state == "quit":
        break

    else:
        print("I don't Understand That...")
    