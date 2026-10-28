import random


def count_cols_no_zeros(m):
    # Пункт 1: считаем столбцы, где нет нулей
    return sum(0 not in [m[i][j] for i in range(len(m))] for j in range(len(m[0])))


def get_char(row):
    # Характеристика: сумма положительных четных
    return sum(x for x in row if x > 0 and x % 2 == 0)


def main():
    r = int(input("Строк: "))
    c = int(input("Столбцов: "))

    # Создаем матрицу
    matrix = [[random.randint(-5, 5) for _ in range(c)] for _ in range(r)]

    print("\nИсходная матрица:")
    for row in matrix: print(row)

    # Вызов функций
    print("\n1. Столбцов без нулей:", count_cols_no_zeros(matrix))

    matrix.sort(key=get_char)
    print("\n2. Отсортированная матрица (по сумме полож. четных):")
    for row in matrix: print(row, "-> сумма:", get_char(row))


if __name__ == "__main__":
    main()