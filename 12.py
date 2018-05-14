source = input('Введите строку (потенциальный палиндром): ')
output = source[::-1]
if source == output:
  print('{color}Слово является палиндромом!{endcolor}'.format(color = '\x1b[1;33;92m', endcolor='\x1b[0m'))
else:
  print('{color}Слово НЕ является палиндромом!{endcolor}'.format(color = '\x1b[1;33;93m', endcolor='\x1b[0m'))