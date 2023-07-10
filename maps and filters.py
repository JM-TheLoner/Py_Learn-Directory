#maps basically take a defined function and use it on a group of things AND RETURNS ALL VALUES
#filter is used to filter the result with parameters given in lambda function
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list(map(lambda x: x+1, nums))) 


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#list function makes it a list.
#map function makes it work on all characters of nums while filter function filters.