s = input('Введите что-нибудь: ')
s = s.split()
l = len(s)
print('Количество слов в строке: {color}{str}{endcolor}'.format(color = '\x1b[1;33;92m', endcolor='\x1b[0m', str = l))
