from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print(s.rfind("Z") - s.find("A") + 1)


if __name__ == '__main__':
    main()
