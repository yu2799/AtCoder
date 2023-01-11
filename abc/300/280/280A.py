from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    res = 0
    for _ in [0] * h:
        s = input()[:-1]
        res += s.count("#")
    print(res)


if __name__ == "__main__":
    main()
