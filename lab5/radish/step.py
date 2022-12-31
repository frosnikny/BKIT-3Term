import math
from radish import given, when, then


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


@given("I have biquadrate equation with coefficients {number1:g} and {number2:g} and {number3:g}")
def have_numbers(step, number1, number2, number3):
    step.context.number1 = number1
    step.context.number2 = number2
    step.context.number3 = number3


@when("I find the roots of it")
def sum_numbers(step):
    step.context.result = sorted(get_roots(
        step.context.number1, step.context.number2, step.context.number3))


@then("I expect the result to be {result:QuotedString}")
def expect_result(step, result):
    lst = result.split(", ")
    if lst[0] == "" and len(lst) == 1:
        lst = [] 

    assert len(step.context.result) == len(lst)
    if len(lst) == 0:
        return
        
    lst = list(map(float, lst))
    assert step.context.result == lst
