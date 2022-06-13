from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    sp = []
    for i in range(n):
        s, p = input().split()
        sp.append((s, -int(p), i + 1))
    sp.sort()
    res = [i[2] for i in sp]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
