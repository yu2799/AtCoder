from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    c = [0] * n
    a = [None] * n
    for i in range(n):
        c[i] = int(input())
        a[i] = set(map(int, input().split()))

    x = int(input())
    c_min = 38
    res = []
    for i in range(n):
        if x in a[i]:
            if c_min > c[i]:
                res = [i + 1]
                c_min = c[i]
            elif c_min == c[i]:
                res.append(i + 1)
    print(len(res))
    print(*res if len(res) else "")


if __name__ == "__main__":
    main()
