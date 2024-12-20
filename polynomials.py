# Программа для вычисления полинома Жегалкина булевой функции по её таблице истинности

def main():
    """
    Эта программа вычисляет полином Жегалкина булевой функции 
    на основе её таблицы истинности, заданной пользователем.
    
    Инструкции:
    1. Введите количество переменных в булевой функции (n).
    2. Введите таблицу истинности в виде 2^n строк, каждая строка содержит:
       значения переменных (0 или 1), разделённые пробелами, затем результат (0 или 1).
    3. Программа выводит полином Жегалкина в канонической форме.
    
    Пример ввода:
    2
    0 0 0
    0 1 1
    1 0 1
    1 1 0

    Пример вывода:
    1 + x1 + x2
    """
    from string import ascii_lowercase as letters
    
    # Считываем количество переменных
    num_of_vars = int(input("Введите количество переменных (n): "))
    if num_of_vars > len(letters):
        raise ValueError("Слишком много переменных. Максимально поддерживаемое количество: {}.".format(len(letters)))
    
    vars = list(letters[:num_of_vars])  # Имена переменных, например ['x1', 'x2', ..., 'xn']
    num_rows = 2 ** num_of_vars

    # Считываем таблицу истинности
    print(f"Введите таблицу истинности в виде {num_rows} строк (значения через пробел, последним идёт результат):")
    table = sorted([tuple(map(int, input().split())) for _ in range(num_rows)])
    
    # Инициализируем результаты
    result, refresh_col = [], [line[-1] for line in table]  # Последний столбец таблицы истинности - это результат функции

    # Добавляем константный член, если он присутствует
    if refresh_col[0]:
        result.append('1')

    # Вычисляем полином Жегалкина с использованием разностей
    for line in range(1, num_rows):
        new_col = []
        for i in range(len(refresh_col) - 1):
            new_col.append(refresh_col[i] ^ refresh_col[i + 1])  # Операция XOR для вычисления разностей

        if new_col[0]:
            params = table[line][:-1]  # Извлекаем значения переменных
            # Формируем моном, комбинируя переменные, где их значение равно 1
            monomial = ''.join([vars[i] for i in range(num_of_vars) if params[i]])
            result.append(monomial)

        refresh_col = new_col  # Обновляем колонку для следующей итерации

    # Выводим полином Жегалкина
    print("Полином Жегалкина:")
    print(' + '.join(result) if result else '0')


if __name__ == "__main__":
    main()
