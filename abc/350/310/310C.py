from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = set()
    for _ in range(n):
        s = input()[:-1]
        if s not in res and s[::-1] not in res:
            res.add(s)
    print(len(res))


if __name__ == "__main__":
    main()
