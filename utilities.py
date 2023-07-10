def find_max(num):
    largest = 0
    for i in num:
        if i > largest:
            largest = i
    return(largest)