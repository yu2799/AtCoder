from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        b[i] = sum(b[i::i]) % 2 ^ a[i]
    print(sum(b))
    res = [i for i in range(n + 1) if b[i] == 1]
    if res:
        print(*res)


if __name__ == "__main__":
    main()
