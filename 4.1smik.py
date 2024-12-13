def print_numbers_between(A, B):
    # Проверяем, что A меньше B
    if A >= B:
        print("А должно бы меньше B.")
        return

    # Создаем список чисел между A и B (не включая A и B).
    numbers = list(range(A + 1, B))

    # Выводим числа в порядке убывания.
    for number in reversed(numbers):
        print(number)

    # Выводим количество чисел
    print("Количество чисел:", len(numbers))


# Пример использования функции

A = 3
B = 10
print_numbers_between(A, B)
