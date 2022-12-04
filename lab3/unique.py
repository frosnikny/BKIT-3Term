class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get("ignore_case", False)
        self.iter = iter(items)
        self.used = set()

    def __next__(self):
        for current in self.iter:
            if isinstance(current, str):
                if (current.lower() if self.ignore_case else current) not in self.used:
                    self.used.add(current.lower())
                    return current
            else:
                if current not in self.used:
                    self.used.add(current)
                    return current
        raise StopIteration

    def __iter__(self):
        return self


def main():
    u = Unique([2, 1, 2, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 4, 5, 4])
    for i in u:
        print(i, end=" ")
    print()
    u = Unique(["A", "a", "B", "b", "b", "B", "A", "C"])
    for i in u:
        print(i, end=" ")
    print()
    u = Unique(["A", "a", "B", "b", "b", "B", "A", "C"], ignore_case=True)
    for i in u:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
