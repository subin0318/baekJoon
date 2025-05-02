# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.    

a=int(input())
k=2
m=[]
while a > 1 :
    if a // k == 0:
        m.append(k)
        break

print(m)