x = int(input('Введите x: '))

print('Числа, которые делятся без остатка на число {}:'.format(x))
for i in range(1,x+1):
    if x % i == 0:
      print(i,end = ' ')

print('\n')