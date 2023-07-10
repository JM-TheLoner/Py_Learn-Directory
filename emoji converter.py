message = input("> ")
words = message.split(" ")
print(words)
emoji = {
    ":)" : "😃",
    ":(" : "😞"
}

#either

for i in words:
    if i in emoji:
        new_msg =  message.replace(i, emoji[i])
    else:
        new_msg = message
print(new_msg)

#or

output = ""
for i in words:
    output += emoji.get(i, i) + " "

print(output)