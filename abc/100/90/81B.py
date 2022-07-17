from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    res = 0
    while True:
        for i in range(len(a)):
            if a[i] % 2:
                print(res)
                return
            a[i] //= 2
        res = res + 1


if __name__ == "__main__":
    main()
