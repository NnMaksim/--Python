month = int(input("введите месяц в виде целого числа "))
month_dict = {1:"январь", 2:"февраль", 3:"март", 4:"апрель", 5:"май", 6:"июнь", 7:"июль", 8:"август", 9:"сентябрь",
10:"октябрь", 11:"ноябрь", 12:"январь"}
month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
              "ноябрь", "январь"]
if month in month_dict:
    print(f"{month} - й месц года {month_list[month - 1]}")