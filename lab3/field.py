def field(items, *args):
    assert len(args) > 0, "Количество искомых аргументов равно 0"

    lst = []
    if len(args) > 1:
        for item in items:
            yield {arg: item[arg] for arg in args}
    else:
        for item in items:
            yield item[args[0]]

    return lst


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    # должен выдавать 'Ковер', 'Диван для отдыха'
    a = []
    for i in field(goods, 'title'):
        a.append(i)
    print(a)

    # должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
    a = []
    for i in field(goods, 'title', 'price'):
        a.append(i)
    print(a)


if __name__ == "__main__":
    main()
