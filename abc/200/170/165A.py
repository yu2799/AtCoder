from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            return
    print("NG")


if __name__ == "__main__":
    main()
