# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# baekjoon
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1


# S=['b','e','a','c','k','j','o','o','n']

# L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# p=[-1]*26

# for i in range (len(L)) :
#     print(L[i], end=" ")
#     if S in L[i] :
#         print("포함")

# a=[1,2,3,4,5]
# b=[1,2,5]

# if b in a :
#     print(b)

# # a와 b 배열 정의
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3,5]

# # 공통 값을 저장할 리스트 초기화
# common_values = [1,1,1,1,1]

# # for문을 사용하여 공통 값 찾기
# for value in a:
#     if value in b:
#         value[b]

# # 결과 출력
# print(common_values)

# a=[-1,-1,-1,-1,-1]
# b=[1,2,3,4,5]

# for i in range (len(a)) :
#     a[i] = b[i]

# print(a)


# a= list(input()) 
# c = 'abcdefghijklmnopqrstuvwxyz'

# for i in c:
#     if i in a:
#        print(a.index(i), end=" ")
#     else:
#         print(-1, end=" ")


# S=['b','e','a','c','k','j','o','o','n']

# L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in L :
#     if i in S :
#        print(S.index(i), end=" ")
#     else :
#         print(-1 , end=" ")

a=[1,2,3,4,5,6]

for i in range (len(a)):
    if a[i] % 2 == 0 :
        print(0,end=" ")
    else :
        print(-1, end=" ")

# 새로 알게 된점 if문만 쓰면 단순 그 조건에 맞는거만 출력이 되는데
# for문 을 쓰게 되면 하나씩 반복 처리하기 때문에 -1 , 0 이렇게 출력이 된다 

# S=list(input())
# L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# for i in L : # L (a,b,c,d ~) 를  i에 대입한다 a,b,c,d = 0,1,3,4 인덱스 값을 가진다
#     if i in S : # 대입한 i에 S 값이 포함 되어 있는지 확인하다
#        print(S.index(i),end=" ") # i에 S 가 있으면  index 값에  a,b,c,d 의 위치를 찾아서 출력한다
#     else:
#         print(-1, end=" ") # 아니면 -1 로 출력하라 

