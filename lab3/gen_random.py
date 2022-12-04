from random import randint


def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield randint(begin, end)


def main():
    a = []
    for i in gen_random(5, 1, 3):
        a.append(i)
    print(a)


if __name__ == "__main__":
    main()
