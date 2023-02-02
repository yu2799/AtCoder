from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a, b = 1, 1
    for _ in range(n):
        ti, ai = map(int, input().split())
        tmp = max(-(-a // ti), -(-b // ai))
        a, b = tmp * ti, tmp * ai
    print(a + b)


if __name__ == "__main__":
    main()
