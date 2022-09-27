from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in [0] * h]
    res = [list(i) for i in zip(*a)]
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
