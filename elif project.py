name = input ("your name is: ")
print("hello " + name)
stand = input("do you watch the English Premier League: ").lower()  #this is so i dont have to put .lower() everytime i call the variable
if stand == "no":
    print("bash")
elif stand == "yes":
        team = input("which EPL Team do you support: ").lower()
        if team == "manchester united":
            print("sorry boss. Nothing lasts forever. Ororo will always hshine again")
        elif team  == "arsenal":
                print("Gunners. A little more effort would be nice")
        elif team == "liverpool":
                    print("you'll never walk alone boss. but salah don dey mess up")
        elif team == "tottenham":
                        print("son and kane. Beta combo")
        elif team == "chelsea":
                                print("HHH-AGBERO. HHH-OKADA DRIVING BASTARD. HHH-ANIMAL")
        elif team == "new castle":
                                print("ARAB MONEY!!!")
        elif team == "manchester city":
                                    print("Olosho supporter")
        elif team != "arsenal" and team != "manchester city" and team != "tottenham" and team != "chelsea" and team != "new castle" and team != "manchester united" and team != "liverpool":
            print("Your club no dey map")

print("END")