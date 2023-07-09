scn_cnt = 0
while True:
    n = int(input())
    scn_cnt += 1
    cnt = [0]*n
    if n == 0:
        break
    student = []
    for _ in range(n):
        student.append(input())
    for _ in range(2*n - 1):
        num, chk = input().split()
        cnt[int(num)-1] += 1
    for i in range(n):
        if cnt[i] != 2:
            print(scn_cnt, student[i])
