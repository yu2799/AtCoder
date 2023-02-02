from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in [0] * k:
        a.append(0)
    print(*a[k:])


if __name__ == "__main__":
    main()
