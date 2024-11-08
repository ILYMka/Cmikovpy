#Задача 1: Вывод целых чисел между A и B в порядке убывания и их количество.
def print_numbers_between(A, B):
    #Проверяем, что A меньше B
    if A>= B:
        print ("А должно бы меньше B.")
        return

    # Создаем список чисел между A и B (не включая A и B).
    numbers = list(range(A + 1, B))

    # Выводим числа в порядке убывания.
    for number in reversed(numbers):
        print (number)

    #Выводим количество чисел
    print("Количество чисел:", len(numbers))
# Пример использования функции
A = 3
B = 10
print_numbers_between (A, B)

# Задача 2: Нахождение наибольшего K, для которого сумма 1 + 2 + ... + K >= N
def find_max_k(N):
    # Проверяем,что N больше 1
    if N <= 1:
        print("N должно быть больше 1.")
        return

    #Инициализируем переменные.
    K = 0
    current_sum = 0

    # Находим K, увеличивая его до тех пор, пока сумма не станет больше или равна N
    while current_sum < N:
        K += 1
        current_sum += K

    # Выводим результат
    print("Наибольшее K:", K)
    print("Сумма от 1 до K:", current_sum)
# Пример использования функции
N = 15
find_max_k(N)


