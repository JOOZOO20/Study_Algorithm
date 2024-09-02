money = [500,100,50,10,5,1]
pay=int(input())
result=0
payback=1000-pay

for i in range(len(money)):
  if payback==0:
    break
  result += payback//money[i]
  payback %= money[i]

print(result)
