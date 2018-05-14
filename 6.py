x = int(input('Введите x: '))

i = 1
print('Все квадраты чисел не превосходящий {}: '.format(x))
while i**i <= x:
      print('Квадрат числа {}: = {}'.format(i, i**i))
      i += 1

print('\n')