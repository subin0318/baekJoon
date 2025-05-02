# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

#  소수 판별
# n= int(input())
# for i in range(1,n+1):
#     count = 0
#     for j in range (1,i+1):
#         if i % j ==0:
#             count +=1
            
#     if count == 2:
#         print(i)
        
n=int(input())

m = list(map(int, input().split()))

k=[]

for i in m: 
    count=0
    for j in range (1,i+1):
        if i % j ==0:
            count +=1
            
    if count == 2:
        k.append(i)
print(len(k))