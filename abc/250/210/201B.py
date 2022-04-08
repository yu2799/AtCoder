n = int(input())
mount = []
for i in range(n):
    s, t = input().split()
    mount.append((int(t), s))
mount.sort(reverse=True)
print(mount[1][1])
