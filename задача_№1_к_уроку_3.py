def div(n1, n2):
    try:
        n1, n2 = int(n1), int(n2)
        n3 = n1 / n2
    except ValueError:
        return 'необходимо ввести число'
    except ZeroDivisionError:
        return 'деление на ноль не допустимо'
    return round(n3, 2)
print(div(input('введите первое число: '), input('введите второе число: ')))