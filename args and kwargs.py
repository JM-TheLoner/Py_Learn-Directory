def func(x, y=7, *args, **kwargs):
    print(kwargs)
    print(*args)

func(1, 2, 3, 4, 5, 6, a=7, b=8)

~