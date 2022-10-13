from sys import stdin


def main():
    input = stdin.readline
    left, right, d = map(int, input().split())
    res = 0
    for i in range(left, right + 1):
        if i % d == 0:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
