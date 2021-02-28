some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in some_list:
    name = item.split(' ')[-1].capitalize()
    print(f'Привет, {name}!')
