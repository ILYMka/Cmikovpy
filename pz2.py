def seconds_since_last_minute(total_seconds):
    """Возвращает количество секунд с начала последней минуты."""
    return total_seconds % 60


if __name__ == "__main__":
    N = int(input("Введите количество секунд с начала суток: "))
    print(seconds_since_last_minute(N))
