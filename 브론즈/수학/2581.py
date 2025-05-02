# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.


n= int(input())
m= int(input())
k=[]

for i in range(n,m+1):
    count = 0
    for j in range (1,i+1):
        if i % j ==0:
            count +=1
            
    if count == 2:
        k.append(i)
        
if len(k) == 0 :
    print(-1)
else : print(sum(k),min(k),sep="\n")