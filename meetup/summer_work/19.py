from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = list(input()[:-1])
    q = int(input())
    flag = False
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            a = (a + n * flag) % (n * 2)
            b = (b + n * flag) % (n * 2)
            s[a], s[b] = s[b], s[a]
        else:
            flag ^= True
    if flag:
        s = s[n:] + s[:n]
    print("".join(s))


if __name__ == "__main__":
    main()
