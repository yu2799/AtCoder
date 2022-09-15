from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(sorted(map(int, input().split())))
    a.append(n + 1)
    res = 0
    diff = []
    prev = 0
    for i in a:
        tmp = i - prev - 1
        if tmp:
            diff.append(tmp)
        prev = i
    if not diff:
        print(0)
        return

    k = min(diff)
    for i in diff:
        res += (i + k - 1) // k
    print(res)


if __name__ == "__main__":
    main()
