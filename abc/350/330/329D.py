from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    vote_cnt = [0] * n
    min_vote = [2 * 10**5 + 1] * (m + 1)
    tmp = 0
    res = []
    for i in a:
        vote_cnt[i - 1] += 1
        if vote_cnt[i - 1] == tmp:
            min_vote[tmp] = min(i, min_vote[tmp])
            res.append(min_vote[tmp])
        elif vote_cnt[i - 1] > tmp:
            tmp += 1
            min_vote[tmp] = i
            res.append(min_vote[tmp])
        else:
            res.append(min_vote[tmp])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
