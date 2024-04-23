a = int(input())
b = int(input())
i = a
sum = 0
while i <= b:
    i+=1
    if i % 9 == 0:
     sum+=i
     print(i)
print(sum)