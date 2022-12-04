import json
from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result
from unique import Unique


path = r"lab3\data_light.json"

with open(path, encoding="utf-8") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, "job-name"), ignore_case=True), key=lambda s: s.lower())


@print_result
def f2(arg):
    return list(filter(lambda s: s[:len("программист")].lower() == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda s: s + " с опытом Python", arg))


@print_result
def f4(arg):
    z = zip(arg, gen_random(len(arg), 100000, 200000))
    return [f"{profession}, зарплата {salary} руб." for profession, salary in z]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

    a = [1, 2, 3, 4]
    a_squares = [i*i for i in a]
    b = list(zip(a, a_squares))
    c = [(i, i*i) for i in a]
    e = list(map(lambda i: (i, i*i), a))
    print(a)
    print(b)
    print(c)
    # rint(d)
    print(e)
