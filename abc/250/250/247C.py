from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = "1"
    if n != 1:
        for i in range(2, n+1):
            res = f"{res} {i} {res}"
    print(res)


if __name__ == '__main__':
    main()
