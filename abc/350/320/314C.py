from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = list(input()[:-1])
    c = list(map(int, input().split()))
    prev = [n for _ in range(m + 1)]
    for i in range(n - 1, -1, -1):
        tmp = c[i]
        if prev[tmp] < n:
            s[i], s[prev[tmp]] = s[prev[tmp]], s[i]
        prev[tmp] = i
    print("".join(s))


if __name__ == "__main__":
    main()
