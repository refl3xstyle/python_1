import numpy as np
mas = np.random.randint(0,1000, int(input('Введите количество элементов в массиве: ')))

print('Элементы сгенерированного массива: ')
for i in range(0,len(mas)):
    print(mas[i], end=' ')

print('\n')
print('\nМаксимальный элемент массива: {color}{str}{endcolor}'.format(color = '\x1b[1;33;92m', str = np.amax(mas), endcolor='\x1b[0m'))
print('\n')
