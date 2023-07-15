#E - 15, S - 28, M - 19
E, S, M = map(int, input().split())

cnt = 1

while True:
    if (cnt - E) % 15 == 0 and (cnt - S) % 28 == 0 and (cnt - M) % 19 == 0:
        break
    cnt += 1

print(cnt)