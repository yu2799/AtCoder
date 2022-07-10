from collections import Counter, defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [input()[:-1] for _ in [0] * n]
    res = Counter(s[0])
    for i in s[1:]:
        c = defaultdict(int)
        for j in i:
            c[j] += 1
        d = defaultdict(int)
        for key, value in res.items():
            d[key] = min(value, c[key])
        res = d
    buf = ""
    for i in sorted(res.keys()):
        buf += i * res[i]
    print(buf)


if __name__ == "__main__":
    main()
