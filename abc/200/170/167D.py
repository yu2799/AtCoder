from sys import stdin


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    visited = set()
    visited.add(0)
    next_visit = a[0]
    teleport = [0]
    cnt = 0
    while next_visit not in visited:
        visited.add(next_visit)
        teleport.append(next_visit)
        next_visit = a[next_visit]
        cnt += 1
    idx = teleport.index(next_visit)
    print(
        teleport[k] + 1
        if k <= idx
        else teleport[(k - idx) % (cnt - idx + 1) + idx] + 1
    )


if __name__ == "__main__":
    main()
