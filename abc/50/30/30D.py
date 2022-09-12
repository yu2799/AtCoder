from sys import stdin


def main():
    input = stdin.readline
    _, a = map(int, input().split())
    k = int(input())
    b = list(map(int, input().split()))
    step = 1
    word = [a]
    word_set = {a}
    while step <= k:
        a = b[a - 1]
        if a in word_set:
            num = word.index(a)
            loop = len(word) - num
            print(word[num + (k - step) % loop])
            break
        else:
            word.append(a)
            word_set.add(a)
            step += 1
    else:
        print(a)


if __name__ == "__main__":
    main()
