from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    q = int(input())
    box = [[] for _ in range(n)]
    num = [set() for _ in range(2 * 10**5)]
    res = []
    for _ in range(q):
        t, *query = map(int, input().split())
        if t == 1:
            i, j = query
            box[j - 1].append(i)
            num[i - 1].add(j)
        elif t == 2:
            res.append(sorted(box[query[0] - 1]))
        else:
            res.append(sorted(list(num[query[0] - 1])))

    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
