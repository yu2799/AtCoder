from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if n == len(set(a)) else "NO")


if __name__ == "__main__":
    main()
