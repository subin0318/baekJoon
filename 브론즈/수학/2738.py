# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

# A=[]
# B=[]


# for _ in range (3):
#     a = list(map(int, input().split()))
#     A.append(a)

# print(A)


# a = [[1, 2, 3], [4, 5, 6], [3, 3, 4]]
# b = [[[1, 2, 3], [4, 5, 6], [3, 3, 4]]]

# # 첫 번째 리스트 요소들 더하기
# result = [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b[0])]

# for i in result:
#     print(*i)


# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

N,M = map(int,input().split())
k=[]
g=[]

for _ in range (N):
    a = list(map(int, input().split()))
    k.append(a)
for _ in range (N):
    b= list(map(int, input().split()))
    g.append(b)

result = [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(k, g)]

for i in result:
    print(*i)