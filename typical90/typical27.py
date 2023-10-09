from sys import stdin


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tmp = sum(abs(i - j) for i, j in zip(a, b))
    print("Yes" if k >= tmp and k % 2 == tmp % 2 else "No")


if __name__ == "__main__":
    main()
