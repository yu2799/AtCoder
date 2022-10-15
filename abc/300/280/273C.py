from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    tmp = {i: idx + 1 for idx, i in enumerate(sorted(set(a)))}
    a_len = len(tmp.keys())
    res = {i: 0 for i in range(n)}
    for i in a:
        res[a_len - tmp[i]] += 1
    print(*res.values(), sep="\n")


if __name__ == "__main__":
    main()
