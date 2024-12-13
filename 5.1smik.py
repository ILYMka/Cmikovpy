def print_stars(m):
    for i in range(1, m + 1):
        print('*' * i)
# Запрашиваем количество строк у пользователя
m = int(input("Введите количество строк (m): "))
print_stars(m)
