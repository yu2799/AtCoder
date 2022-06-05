from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(input()) for _ in [0] * n]
    tmp = sorted(set(a))
    d = {i: idx for idx, i in enumerate(tmp)}
    res = [d[i] for i in a]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
