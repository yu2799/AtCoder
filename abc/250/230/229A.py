s1 = list(input())
s2 = list(reversed(input()))
if s1.count("#") == 2 and s2.count("#") == 2:
    print("Yes")
elif s1 == s2:
    print("No")
else:
    print("Yes")
