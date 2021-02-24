num = int(input('Введите число от 0 до 20 '))
ending_ov = 'ов'
ending_a = 'а'

percent = ''
exep = [11, 12, 13, 14]

if 5 <= num % 10 <= 9 or num % 10 == 0 or num in exep:
    percent = ending_ov
elif 2 <= num % 10 <= 4:
    percent = ending_a
else:
    percent = ''


print(num,'процент{}'.format(percent))

print('Все сколонения для проверки:')
numbers = []
for i in range(21):
    numbers.append(i)
for number in numbers:
    if 5 <= number % 10 <= 9 or number % 10 == 0 or number in exep:
        percent = ending_ov
    elif 2 <= number % 10 <= 4:
        percent = ending_a
    else:
        percent = ''

    print(number,'процент{}'.format(percent))
