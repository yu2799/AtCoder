from sys import stdin


def main():
    input = stdin.readline
    n, _ = input().split()
    d = list(map(int, input().split()))
    while True:
        for i in str(n):
            if int(i) in d:
                break
        else:
            print(n)
            return
        n = int(n) + 1


if __name__ == "__main__":
    main()
