a=int(input())
b=int(input())
c=int(input())

if (c >= (a + b)) or (b >= (a + c)) or (a >= (b + c)):
  print ("Нет, треугольник не существует!")
else:
  print ("Да, треугольник существует!")