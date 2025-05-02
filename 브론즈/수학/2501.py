k=[]

a,b=map(int,input().split())

for i in range (1,a+1):
    if a % i == 0:
        k.append(i)

# if b > len(k):
#    print(0)
# else: print(k[b-1])    

print(0 if b > len(k) else k[b-1])