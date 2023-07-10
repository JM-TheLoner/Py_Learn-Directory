import bisect


a = [12, 13, 14, 53, 145, 14, 21, 475]
a.sort()


i = bisect.bisect_left(a, 17)
print(i)

bisect.insort_left(a, 17)
print(a)

d = bisect.bisect_right(a, 14)
print(d)

bisect.insort_right(a, 19)
print(a)

# def find_next(a, x):
#     i = bisect.bisect_right(a, x)
#     if i < len(a):
#         return a[i]
#     return False

# print(find_next([10, 12, 20, 24, 56], 23))



# def get_grade(score, cutoffs=[60,70,80,90], grades = 'FDCBA'):
#     i = bisect.bisect_right(cutoffs, score)
#     return grades[i]

# grades = [get_grade(score) for score in [52,99,77,70,89,90,100]]
# print(grades)