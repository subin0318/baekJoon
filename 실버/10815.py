# a=[6,3,2,10,-10]
# b=[10 , 9 ,  -5 , 2 , 3,  4,  5, -10]
# k=[]

# for i in range(len(b)):
#     if b[i] in a :
#         k.append(1)
#     else:  k.append(0)
# print(k)


N=int(input())
a=list(map(int, input().split()))
M=int(input())
b=list(int,input().split())
k=[]

for i in range(len(b)):
    if b[i] in a :
        k.append(1)
    else:  k.append(0)
print(*k)
