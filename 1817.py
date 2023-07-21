N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    book = list(map(int, input().split()))
    #print(book)
    cnt = 1
    tmp = M
    while len(book) != 0:
        if book[0] <= tmp:
            tmp = tmp - book[0]
            del book[0]        

        if len(book) == 0:
            break

        if tmp < book[0]:
            tmp = M
            cnt += 1

    print(cnt)