a = int(input())
i = 1
while i <= a:
    cnt = 0
    j = 1
    while j <= i:
        if i % j == 0:
            cnt+=1
        j+=1
    if cnt > 2:
        print(i, ' ')
    i+=1



