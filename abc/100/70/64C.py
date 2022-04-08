from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 9
    for i in a:
        if i < 3200:
            cnt[i//400] = 1
        else:
            cnt[8] += 1
    if sum(cnt[:-1]) == 0:
        print(1, str(cnt[8]))
    else:
        print(cnt[:-1], sum(cnt))


if __name__ == '__main__':
    main()
