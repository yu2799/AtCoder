from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    res = 0
    for left in range(n + 1):
        for right in range(n + 1):
            back = k - left - right
            if back < 0 or n < left + right:
                continue

            tmp = 0
            q = []
            for i in range(left):
                tmp += v[i]
                q.append(v[i])
            for i in range(right):
                tmp += v[n - i - 1]
                q.append(v[n - i - 1])

            q.sort(reverse=True)
            while q and back > 0 and q[-1] < 0:
                tmp -= q.pop()
                back -= 1
            if res < tmp:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
