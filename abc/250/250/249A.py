from sys import stdin


def solve(a, b, c, x):
    res = 0
    while x > 0:
        if a <= x:
            res += a * b
            x -= a + c
        else:
            res += x * b
            x = 0
    return res


def main():
    input = stdin.readline
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = solve(a, b, c, x)
    aoki = solve(d, e, f, x)
    if takahashi < aoki:
        print("Aoki")
    elif takahashi > aoki:
        print("Takahashi")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
