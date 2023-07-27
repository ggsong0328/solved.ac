N = int(input())
card = []
dump = []
for i in range(N):
    card.append(i+1)
#print(card)

while len(card) != 1:
    dump.append(card[0])
    del card[0]
    card.append(card[0])
    del card[0]

dump.append(card[0])

for i in range(len(dump)):
    print(dump[i], end=' ')