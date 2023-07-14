s = str(input())
cnt_1 = 0
cnt_0 = 0
for i in range(len(s)-1):
    if s[i] != s[i+1] and s[i] == '1':
        cnt_1 += 1
    elif s[i] != s[i+1] and s[i] == '0':
        cnt_0 += 1
if cnt_1 >= cnt_0:
    print(cnt_1)
else:
    print(cnt_0)

