#이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 
# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
#정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

# k = [3, 0, 4, 0]

# # for i in range(len(k)):
# #     if k[i] != 0:
# #        print(k.index(k[i]))

# print(k[len(k)-1])

k=int(input())

p=[]

for _ in range (k):
    i=int(input())
    
    if i==0 :
       p.pop()
    else: p.append(i)
       

print(sum(p))

