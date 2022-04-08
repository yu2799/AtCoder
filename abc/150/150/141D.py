from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    cnt = 0
    while cnt < m:
        tmp = a[0] / 2
        for i in range(n):
            if a[0] == 0:
                cnt = m
            if a[i] > tmp:
                a[i] //= 2
                cnt += 1
                if cnt == m:
                    break
            else:
                a.sort(reverse=True)
                break
    print(sum(a))


if __name__ == "__main__":
    main()
