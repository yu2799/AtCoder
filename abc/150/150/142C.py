from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = {i: idx for idx, i in enumerate(map(int, input().split()))}
    res = [a[i] + 1 for i in sorted(a.keys())]
    print(*res)


if __name__ == "__main__":
    main()
