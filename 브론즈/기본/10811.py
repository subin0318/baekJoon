# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 바구니는 일렬로 놓여져 있고, 
# 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다. 

# for i in range (5,0,-1) :
#     print(i)

# 5 4
# 1 2
# 3 4
# 1 4
# 2 2

# 3 4 1 2 5

#a[0:3] = a[0:3][::-1] 

# N,M = map(int,input().split())

# a=[_ for _ in range(1,N+1)]

# print(a)

# for _ in range (M) :
#     i,j=map(int,input().split())
#     a[i-1:j]=a[i-1:j][-1]

# print(*a)


N,M = map(int,input().split())

a=[_ for _ in range(1,N+1)]

for _ in range (M):
    i,j=map(int,input().split())
    a[i-1:j] = a[i-1:j][::-1] # 원하는 구간을 역순으로 정렬하는 방법 

print(*a)