N = int(input())
vote = []
for _ in range(N):
    vote.append(int(input()))
cnt = 0
while max(vote) != vote[0]:
    idx = vote.index(max(vote))
    vote[idx] -= 1
    vote[0] += 1
    cnt += 1

if vote.count(max(vote)) > 1:
    print(cnt + 1)
else:
    print(cnt)
    