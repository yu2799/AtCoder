from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    score = [0] * n
    for i in range(n):
        score[i] = sum(map(int, input().split()))
    border = sorted(score, reverse=True)[k-1] - 300

    res = []
    for i in score:
        if border <= i:
            res.append("Yes")
        else:
            res.append("No")
    print(*res, sep="\n")


if __name__ == '__main__':
    main()
