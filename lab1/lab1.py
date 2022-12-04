import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число с проверкой
    while True:
        try:
            coef = float(coef_str)
            break
        except:
            print("Введено неверно, повторите попытку")
            print(prompt)
            coef_str = input()

    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if root > 0:
            root1 = math.sqrt(root)
            root2 = -math.sqrt(root)
            result.append(root1)
            result.append(root2)
        elif root == 0:
            result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        first_root = (-b + sqD) / (2.0*a)
        second_root = (-b - sqD) / (2.0*a)
        if first_root > 0:
            root1 = math.sqrt(first_root)
            root2 = -math.sqrt(first_root)
            result.append(root1)
            result.append(root2)
        elif first_root == 0:
            result.append(first_root)
        if second_root > 0:
            root3 = math.sqrt(second_root)
            root4 = -math.sqrt(second_root)
            result.append(root3)
            result.append(root4)
        elif second_root == 0:
            result.append(second_root)

    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, {}'.format(
            roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# lab1.py 1 0 -4
