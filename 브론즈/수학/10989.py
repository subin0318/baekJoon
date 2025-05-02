a=int(input())
b=[]

for _ in range (a):
    c=int(input())
    b.append(c)
b.sort()
print(*b) 