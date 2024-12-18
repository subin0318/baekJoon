# 영수증에 적힌,
# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

# 260000
# 4
# 20000 5
# 30000 2
# 10000 6
# 5000 8

# YES 

a=int(input())
b=int(input())
c=[]

for i in range (1,b+1):
    d,e=map(int,input().split())
    c.append(d*e)

if a == sum(c) : print("Yes")
else : print("No")