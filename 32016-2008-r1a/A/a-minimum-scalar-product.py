# https://code.google.com/codejam/contest/32016/dashboard#s=p0
t = int(raw_input())
cc = 1
while t > 0:
    n = int(raw_input())
    s = raw_input()
    s = s.split()
    a = [int(x) for x in s]
    s = raw_input()
    s = s.split()
    b = [int(x) for x in s]
    a.sort()
    b.sort()
    b.reverse()
    res = 0
    for i in range (0, len(a)):
        res += a[i] * b[i]
    print("Case #" + str(cc) + ": " + str(res))
    t -= 1
    cc += 1
