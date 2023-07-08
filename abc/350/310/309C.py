from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    ab = []
    tmp = 0
    for _ in range(n):
        a, b = map(int, input().split())
        tmp += b
        ab.append((a, b))
    ab.sort()
    prev = 0
    for a, b in ab:
        if tmp <= k:
            break
        prev = a
        tmp -= b
    print(prev + 1)


if __name__ == "__main__":
    main()
