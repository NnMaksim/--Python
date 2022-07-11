my_list = ["Abc", 7 != 2, 2, 3.4, 5+8j, [1, 2], (3, 4.5, 6)]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")
