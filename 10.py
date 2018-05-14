
try:
    c = int(input("Введите что-нибудь: "))
    print("Введеное вами это {color}ЧИСЛО{endcolor}".format(color = '\x1b[1;33;92m', endcolor='\x1b[0m'))
except ValueError:
    print("Введеное вами это {color}НЕ ЧИСЛО{endcolor}, попробуйте снова!".format(color = '\x1b[1;33;93m', endcolor='\x1b[0m'))
