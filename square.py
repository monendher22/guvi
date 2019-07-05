q=int(input())
sum=0
while(q>0):
    dig=q%10
    sum=sum+dig*dig
    q=q//10
print(sum)
