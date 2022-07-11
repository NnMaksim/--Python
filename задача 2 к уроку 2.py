my_list = list(input('Введите число '))
for r in range(1, len(my_list), 2):
    my_list[r - 1], my_list[r] = my_list[r], my_list[r - 1]
print(my_list)

