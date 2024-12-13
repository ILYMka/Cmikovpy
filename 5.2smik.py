def main(invert_digits):
    # Список для хранения пяти хранения пяти целых положительных чисел
    numbers = []

    # Считываем пять целых положительных чисел
    for i in range(5):
        while True:
            try:
                num = int(input(f"Введите целое положительное число {i + 1}: "))
                if num > 0:
                    numbers.append(num)
                    break
                else:
                    print("Число должно быть положительным. Попробуйте снова. ")
            except ValueError:
                print("Некорректный ввод. Введите целое число. ")
                # Меняем порядок следования цифр на обратный для каждого из введенных чисел
                inverted_numbers = [invert_digits(num) for num in numbers]
                # Выводим результаты
                for original, inverted in zip(numbers, inverted_numbers):
                    print(f"Оригинальное число: {original}, Инвертированное число {inverted}")
        if __name__ == "__main__":
            main(invert_digits)
