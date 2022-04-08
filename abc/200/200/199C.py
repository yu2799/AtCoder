from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = list(input()[:-1])
    q = int(input())
    frip = False
    for _ in [0] * q:
        t, a, b = map(int, input().split())
        if t == 1:
            a -= 1
            b -= 1
            if frip:
                a = (a + n) % (2 * n)
                b = (b + n) % (2 * n)
            s[a], s[b] = s[b], s[a]
        else:
            frip ^= True

    if frip:
        print(*(s[n:] + s[:n]), sep="")
    else:
        print(*s, sep="")


if __name__ == "__main__":
    main()
