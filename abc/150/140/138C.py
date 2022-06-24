from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for _ in [0] * (n - 1):
        v.append((v[0] + v[1]) / 2)
        v.pop(0)
        v.pop(0)
        v.sort()
    print(v[0])


if __name__ == "__main__":
    main()
