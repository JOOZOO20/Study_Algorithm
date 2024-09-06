a,b=input().split()
a=list(a)
b=list(b)
max_a=a.copy()
min_a=a.copy()
max_b=b.copy()
min_b=b.copy()

for i in range(len(a)):
    if a[i]=='5':
        max_a[i]='6'
    elif a[i]=='6':
        min_a[i]='5'

for i in range(len(b)):
    if b[i]=='5':
        max_b[i]='6'
       
    elif b[i]=='6':
        min_b[i]='5'
        
    
max_a = ''.join(max_a)
min_a = ''.join(min_a)
max_b = ''.join(max_b)
min_b = ''.join(min_b)


max_a=int(max_a)
min_a=int(min_a)
max_b=int(max_b)
min_b=int(min_b)

min = min_a + min_b
max = max_a + max_b

print(min,max)