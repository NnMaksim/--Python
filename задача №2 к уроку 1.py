time = int (input("Введите время в секундах: "))
hours = time // 3600
minute = ((time - hours * 3600) // 60)
secunda = (time - hours * 3600 - minute * 60)
print(hours,":", minute,":", secunda)