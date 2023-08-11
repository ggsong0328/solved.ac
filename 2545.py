import sys
T = int(sys.stdin.readline())
ans = []
for _ in range(T):
	input()
	A, B, C, D = map(int, sys.stdin.readline().split())
	A, B, C = sorted((A, B, C))
	S = A + B + C - D
	tmp = min(S // 3, A)
	A = tmp
	S -= tmp
	tmp = min(S // 2, B)
	print(A * tmp * (S-tmp))
		