my_str = input("введите строку из нескольких слов. ").split()
for i, word in enumerate(my_str, 1):
    print (f"{i}. {word[:10]}")