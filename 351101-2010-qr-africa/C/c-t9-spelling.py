letters = "abcdefghijklmnopqrstuvwxyz "
keys = ["2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55",\
        "555", "6", "66", "666", "7", "77", "777", "7777", "8", "88", \
        "888", "9", "99", "999", "9999", "0"]

#for i in range (0, len(letters)):
#    print(letters[i], keys[i])

n = int(raw_input())
cc = 1
while n > 0:
    s = raw_input()
    res = ""
    prev = None
    for x in s:
        if keys[letters.index(x)][0] == prev:
            res += " " + keys[letters.index(x)]
        else:
            res += keys[letters.index(x)]
        prev = keys[letters.index(x)][0]
    print("Case #" + str(cc) + ": " + res)
    n -= 1
    cc += 1
