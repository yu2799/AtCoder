from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = [list(input()[:-1]) for _ in [0] * n]
    ns = []
    for i in range(n):
        tmp = set()
        for j in range(m):
            if s[i][j] == "o":
                tmp.add(j)
        ns.append(tmp)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(ns[i] | ns[j]) == m:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
