from sys import stdin


def main():
    input = stdin.readline
    a, b = input().split()
    a = int(a)
    if "." in b:
        b, c = map(int, b.split("."))
    else:
        b = int(b)

    print(a * (b * 100 + c) // 100)


if __name__ == "__main__":
    main()
