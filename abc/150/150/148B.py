n = int(input())
s, t = input().split()
for i, j in zip(s, t):
    print(i + j, end="")
