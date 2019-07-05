s = int(input(''))
total = 0
while(n>=0):
  dig = s%10
  total = total + dig*dig
  s = s//10
print(total)
