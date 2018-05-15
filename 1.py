def check_year(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return print('{} - Обычный год'.format(year))
    else:
        return print('{} - Високосный год'.format(year))

# Выбор варианта рассчета
try:
    flag = int(input('Выберите из один вариантов программы: \n1 - посмотреть конкретный год\n2 - посмотреть диапозон лет\n'))
except KeyError as e:
    raise ValueError('Введите только 1 или 2, ошибка: {}'.format(e.args[0]))

if (flag == 1):
    year = int(input('Введите интересуемый год: '))
    check_year(year)
elif (flag == 2):
    start = int(input('Введите первое число года: '))
    end = int(input('Введите второе число года: '))
    for i in range(start,end):
        check_year(i)
else:
    print('Выберите только 1 или 2!')




