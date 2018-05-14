#Вводим число
year = int(input())

# Сразу проверяются все условия.
# Если год не делится на 4 или делится на 100, но не на 400,
# то он обычный. Во всех остальных случаях - високосный.
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("usual year")
else:
    print("intercalary year")