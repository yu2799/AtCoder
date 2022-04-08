n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
print(sum([i for i in a[::2]]) - sum([i for i in a[1::2]]))
