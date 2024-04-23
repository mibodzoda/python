a = int(input())
i = 0
sum = 0
while i <= a*2:
   
    if i % 2 != 0:
        sum +=i
        print(i)
    i+=1
print(sum)