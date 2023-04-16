from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    q = int(input())
    two = [[] for _ in range(n)]
    three = [set() for _ in range(2 * 10**5)]
    res = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            i = query[1]
            j = query[2]
            two[j - 1].append(i)
            three[i - 1].add(j)
        elif query[0] == 2:
            res.append(sorted(two[query[1] - 1]))
        else:
            res.append(sorted(list(three[query[1] - 1])))
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
