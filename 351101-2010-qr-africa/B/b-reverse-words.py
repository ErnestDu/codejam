n = int(raw_input())
cc = 1
while n > 0:
    s = raw_input()
    s = s.split()
    s.reverse()
    ss = ""
    for x in s:
        ss += " " + x
    print("Case #" + str(cc) + ":" + ss)
    n -= 1
    cc += 1
