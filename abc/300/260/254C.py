from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = [list(sorted(a[i::k])) for i in range(k)]
    print("Yes" if tmp == sorted(tmp) else "No")


if __name__ == "__main__":
    main()
