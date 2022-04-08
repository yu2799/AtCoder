n = input()
for i in range(len(n)+1):
    s = "0"*i + n
    if s == s[::-1]:
        print("Yes")
        exit()
print("No")

"""
n = list(input())
cnt = 0
for i in range(len(n)-1, -1, -1):
    if n[i] != "0":
        if n[:i+1] == list(reversed(n[:i+1])):
            print("Yes")
            exit()
        else:
            print("No")
            exit()
print("Yes")
"""
