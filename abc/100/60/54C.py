from sys import stdin
from itertools import permutations


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    ab = set()
    for _ in [0] * m:
        a, b = map(lambda x: int(x) - 1, input().split())
        ab.add((a, b))
        ab.add((b, a))

    fact = 1
    for i in range(1, n):
        fact *= i
    res = 0
    permutation = list(permutations(range(n)))
    for i in range(fact):
        visited = [False] * n
        prev = 0
        if permutation[i][0] != 0:
            break
        for j in permutation[i][1:]:
            if (prev, j) in ab and not visited[j]:
                visited[j] = True
                prev = j
                continue
            else:
                break
        else:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
