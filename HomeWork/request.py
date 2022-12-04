import requests


def request(n: int):
    url = "http://127.0.0.1:5000/"
    res = url + '/num/' + str(n)
    r = requests.get(res, timeout=(10, 10))
    try:
        data = r.json()
    except:
        data = r.text
    return data


def main():
    n = input("Enter the number of numbers: ")
    print(request(n))
    n = input("Enter the number of numbers: ")
    print(request(n))


if __name__ == "__main__":
    main()
