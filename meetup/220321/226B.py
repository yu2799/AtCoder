from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = set()
    for _ in [0] * n:
        _, *a = map(int, input().split())
        res.add(tuple(a))
    print(len(res))


if __name__ == "__main__":
    main()
