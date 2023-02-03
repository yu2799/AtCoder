from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 100
    for _ in range(n):
        t = int(input())
        if res > t:
            res = t
    print(res)


if __name__ == "__main__":
    main()
