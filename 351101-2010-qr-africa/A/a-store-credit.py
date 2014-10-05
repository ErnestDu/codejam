n = int(raw_input())
cc = 1
while n > 0:
    c = int(raw_input())
    i = int(raw_input())
    s = raw_input()
    s = s.split()
    num = [int(x) for x in s]
    flag = 0
    for x in range (0, len(num)):
        for y in range (x + 1, len(num)):
            if num[x] + num[y] == c:
                print("Case #" + str(cc) + ": " + str(x + 1) + " " + str(y + 1))
                flag = 1
                break
        if flag == 1:
            break
    n -= 1
    cc += 1
