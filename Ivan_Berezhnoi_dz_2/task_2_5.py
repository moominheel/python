prices = [57.8, 46.51, 97, 17.99, 139.98, 26.5, 84.01, 38.14, 15, 9.24]
# 5A
prices_str = []
prices_split = []

for price in prices:
    prices_str.append(str(price))

for item in prices_str:
    x = item.split('.')[0]
    y = item.split('.')[-1]
    if item.isdigit():
        y = '00'
    if len(y) == 1:
        y = int(y) * 10
    prices_split.append(f'{int(x):02d} руб {y} коп')

prices_split_1 = ', '.join(prices_split)
print(prices_split_1)

# 5B
# print(id(prices_split))
# prices_split.sort()
# print(prices_split, id(prices_split))
# список сортируется неправильно, трехначное число сортируется, как двухзначное, вместо 139 как будто видит 13.
# Не понял, как это исправить. Но список остается тем же, id совпадают.

# 5C
prices.sort(reverse=True)
prices_str = []
prices_split = []

for price in prices:
    prices_str.append(str(price))

for item in prices_str:
    x = item.split('.')[0]
    y = item.split('.')[-1]
    if item.isdigit():
        y = '00'
    if len(y) == 1:
        y = int(y) * 10
    prices_split.append(f'{int(x):02d} руб {y} коп')

print(prices_split)
# 5D
top5 = prices_split[:5]
top5.reverse()
print(top5)
