phrase_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
               'была', '+5', 'градусов']

new_list = []

for item in phrase_list:
    if item.isnumeric():
        new_list.append('"')
        new_list.append(f'{int(item):02d}')
        new_list.append('"')
    # if item.split()[-1].isdigit():
    #     new_list.append('"')
    #     new_list.append(f'{int(item):02d}')
    #     new_list.append('"')

    else:
        new_list.append(item)
print(new_list)

new_list = ' '.join(new_list)
print(new_list)
