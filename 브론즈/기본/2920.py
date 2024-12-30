# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

# a=[1,2,3,4,5,6,7,8]
# b=[1,2,3,4,5,6,7,8]

# print(a==b)

a=[1,2,3,4,5,6,7,8]
b=[8 ,7, 6, 5, 4, 3, 2, 1]

c=list(map(int,input().split()))


if c == a : print("ascending")
elif c==b : print("descending")
else : print("mixed")