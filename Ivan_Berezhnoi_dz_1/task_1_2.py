numbers = []

for i in range(1000):
    if i % 2 != 0:
        numbers.append(i ** 3)




all_sum = 0
for number in numbers:
    sugar = number
    sum_n = 0
    sum_list = []
    x = len(str(number)) - 1

    for i in range(len(str(number))):
        sum_list.append(number // 10 ** x)
        number -= (10 ** x) * sum_list[i]
        x -= 1

    for i in sum_list:
        sum_n += i
    if sum_n % 7 == 0:
        all_sum += sugar



print(all_sum)

all_sum_sev = 0
for number in numbers:
    number = number + 17
    an_sugar = number
    sum_sev = 0
    sum_sev_list = []
    y = len(str(number)) - 1

    for i in range(len(str(number))):
        sum_sev_list.append(number // 10 ** y)
        number -= (10 ** y) * sum_sev_list[i]
        y -= 1
    for i in sum_sev_list:
        sum_sev += i
    if sum_sev % 7 == 0:
        all_sum_sev += an_sugar

print(all_sum_sev)




