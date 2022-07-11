def my_func(n_1, n_2, n_3):
    try:
        my_list = list(map(float, [n_1, n_2, n_3]))
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError, ValueError):
        return "Введите число!"


print(my_func(input(), input(), input()))