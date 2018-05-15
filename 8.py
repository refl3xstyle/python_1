import numpy as np
mas = np.random.randint(-100,100, (int(input('Введите количество элементов в массиве: '))))
print('Сгенерированные числа массива: ')
for i in range(0,len(mas)):
    print(mas[i], end=' ')

for i in range(1, len(mas) - 1):
    if ((mas[i-1] > 0) and (mas[i+1] > 0)):
        str = '{color_success}Выполняется!{endcolor}'.format(color_success='\x1b[1;33;92m', endcolor='\x1b[0m')
    else:
        str = '{color_wrong}Не выполняется!{endcolor}'.format(color_wrong='\x1b[1;33;91m', endcolor='\x1b[0m')

print('\nCоседние элементы с одинаковым знаком. Условие: {}'.format(str))