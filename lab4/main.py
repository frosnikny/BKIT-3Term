import math
import pytest


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


class TestRoots:
    def test_0roots(self):
        assert len(get_roots(1, 0, 10)) == 0

    def test_2roots(self):
        a = get_roots(1, 0, -16)
        assert (len(a) == 2) and (2 in a) and (-2 in a)

    def test_3roots(self):
        a = get_roots(-4, 16, 0)
        assert (len(a) == 3) and (0 in a) and (2 in a) and (-2 in a)

    def test_4roots(self):
        a = get_roots(1, -5, 6)
        assert (len(a) == 4) and (math.sqrt(3) in a) and (math.sqrt(3) in a)\
            and (math.sqrt(2) in a) and (-math.sqrt(2) in a)
