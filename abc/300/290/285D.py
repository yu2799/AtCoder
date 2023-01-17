from collections import defaultdict, deque
from sys import stdin


def topological_sort(g, into_num):
    q = deque()
    for i in g.keys():
        if into_num[i] == 0:
            q.append(i)
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in g[v]:
            into_num[adj] -= 1
            if into_num[adj] == 0:
                q.append(adj)
    return ans


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(list)
    into_num = defaultdict(int)
    tmp = set()
    for _ in [0] * n:
        s, t = input().split()
        d[s].append(t)
        into_num[t] += 1
        tmp.add(s)
        tmp.add(t)
    res = topological_sort(d, into_num)
    print("Yes" if len(res) == len(tmp) else "No")


if __name__ == "__main__":
    main()
