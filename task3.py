a = int(input())
sum = 0
while a >= 1 :
    sum+= a%10
    a//=10
print(sum)