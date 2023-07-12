group = []
groups = []
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        inp = input().split()
        group.append(inp)
    groups.append(group)
    group = []
#print(group)
for i in range(len(groups)):
    if i != 0:
        print()
    cnt = 0
    print(f'Group {i + 1}')
    for j in range(len(groups[i])):
        bad = -1
        if 'N' in groups[i][j]:
            nasty = groups[i][j].count('N')
            for k in range(nasty):
                bad = groups[i][j].index('N', bad + 1)
                badp = (len(groups[i]) + j - bad)%len(groups[i])
                print(f'{groups[i][badp][0]} was nasty about {groups[i][j][0]}')
            cnt += 1
    if cnt == 0:
        print('Nobody was nasty')

