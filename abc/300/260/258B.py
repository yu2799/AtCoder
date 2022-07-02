from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [list(input()[:-1]) for _ in [0] * n]
    res = set()
    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += a[i][j]
        for j in range(n):
            res.add(int(tmp[j:] + tmp[:j]))
            res.add(int((tmp[j:] + tmp[:j])[::-1]))
    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += a[j][i]
        for j in range(n):
            res.add(int(tmp[j:] + tmp[:j]))
            res.add(int((tmp[j:] + tmp[:j])[::-1]))
    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += a[j % n][(i + j) % n]
        for j in range(n):
            res.add(int(tmp[j:] + tmp[:j]))
            res.add(int((tmp[j:] + tmp[:j])[::-1]))
    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += a[j % n][(n - i - j) % n]
        for j in range(n):
            res.add(int(tmp[j:] + tmp[:j]))
            res.add(int((tmp[j:] + tmp[:j])[::-1]))

    print(max(res))


if __name__ == "__main__":
    main()
