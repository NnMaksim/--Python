n = str(input("Введите целое число:"))
num_2 = f"{n}{n}"
num_3= f"{n}{num_2}"
print(n, "+", num_2 ,"+", num_3, "=", F'{int(n) + int(num_2) + int(num_3)}')

