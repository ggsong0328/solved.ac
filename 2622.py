import sys
n = int(sys.stdin.readline())
cnt = 0
for x in range((n+1)//3, (n+1)//2):
	cnt += (3*x - n + 2) // 2
print(cnt)
