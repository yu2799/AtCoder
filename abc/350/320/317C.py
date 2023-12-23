from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))


if __name__ == "__main__":
    main()
