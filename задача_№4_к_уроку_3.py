def my_func(x, y):
    try:
        r = x ** y
    except TypeError:
        return "что это? только целое число"
    return r
print(int(input()), int(input()))