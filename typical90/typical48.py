from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    score = []
    for _ in [0] * n:
        a, b = map(int, input().split())
        score.append(a-b)
        score.append(b)
    score.sort(reverse=True)
    print(sum(score[:k]))


if __name__ == '__main__':
    main()
