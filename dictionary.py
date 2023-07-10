animals = {
    "sonic":"hedgehog",
    "shadow":"hedgehog",
    "silver":"hedgehog",
    "tails":"fox"
} 
animals["rogue"] = "bat"
print(animals.get("sonic"))
print(animals)
print(animals.get("rogue"))
print("sonic" in animals)
print("fox" in animals)

animals.pop("sonic")
print(animals)

animals["tails"] = "news"
print(animals)

if "hedgehog" in animals:
    print("yes")
else:
    print("no") 


for i in animals:
    if animals[i] == "hedgehog":
        print(i)


#dictionaries store data as seen above but the second part of the data isnt part of the dictionary
#its assigned to its corresponding first part
