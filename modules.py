import definition

#the module you import from must be in the same group as the module you import to

a = definition.percentage(12, 32)
s = definition.even(23)

print(a)
print(s)

#or

from definition import percentage

a = percentage(24, 134)
print(a)