from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    flag = [False] * n
    res = [0] * n
    for _ in [0] * m:
        p, s = input().split()
        if not flag[int(p) - 1]:
            if s == "WA":
                res[int(p) - 1] += 1
            else:
                flag[int(p) - 1] = True
    print(sum(flag), sum([res[i] for i in range(n) if flag[i]]))


if __name__ == "__main__":
    main()
