a = int(input())
b = int(input())
c = int(input())
d = int(input())

count = 0

for a in range(b):
    if ((a % d) == c):
        print('Подходящее значение найдено: "{}"'.format(a))
        count += 1
    a += 1

if count == 0:
    print("Значений в данном диапозоне и с таким остатком не найдено!")